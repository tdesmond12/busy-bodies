# Captures app screenshots for the user guide. Run from the repo root with a local server on :8765.
import asyncio
from playwright.async_api import async_playwright
OUT = 'docs/img/'
SEED = r"""(async()=>{
  nutritionSettings().fastOn = true; nutritionSettings().fastPlan = '16';
  await startMilestone('first-pushup', 2); await startProgram('meditation','addon',[...WEEK],10);
  const add = async (d, name, ex) => { const w={date:d,dayName:name,exercises:ex,cardioMin:0,notes:'',createdAt:Date.now()+Math.random()}; const id=await S.store.addWorkout(w); S.workouts.unshift({...w,id}); };
  const P = plan().days;
  for(let k=1;k<=6;k++){ const base=shiftDate(todayStr(),-k*3); await add(base, P[k%P.length].name, P[k%P.length].exercises.slice(0,3).map((id,i)=>({id,name:EXBY[id].name,pattern:EXBY[id].p,sets:[{w:usesWeight(EXBY[id])?40+k*5:'',r:10},{w:usesWeight(EXBY[id])?40+k*5:'',r:9}]})));
    await add(base, 'First push-up practice', [{id:'waist-high-push-up',name:'Waist-High Push-Up',pattern:'push_h',sets:[{r:6+Math.floor(k/2)},{r:6},{r:5}],ms:{id:'first-pushup',level:2}}]); }
  S.workouts.sort((a,b)=>b.date.localeCompare(a.date));
  S.account.bodyLog = []; for(let i=40;i>=0;i-=2) S.account.bodyLog.push({date:shiftDate(todayStr(),-i), lb: Math.round((201 - (40-i)*0.12 + Math.sin(i)*0.8)*10)/10}); S.account.bodyGoal = 185;
  await saveAccount();
  const days = JSON.parse(localStorage.getItem('rr.days')||'{}');
  for(let i=0;i<14;i++){ const dt=shiftDate(todayStr(),-i); days[dt] = {...emptyDay(), water: 48+(i%3)*8,
    fast:{first: i%4===2?'10:45':'12:15', last:'19:45'}, sleep:{bed:'22:50', wake:'06:1'+(i%9), wakes: i%2?[{at:'03:10',min:15}]:[]},
    meals:[{name:'Greek yogurt & berries',type:'Breakfast',cal:260,protein:22,carbs:30,fat:5,sugar:18,fiber:4},{name:'Chicken salad',type:'Lunch',cal:520,protein:42,carbs:20,fat:28,sugar:6,fiber:7},{name:'Salmon, rice & broccoli',type:'Dinner',cal:640,protein:40,carbs:55,fat:24,sugar:4,fiber:6}]}; }
  localStorage.setItem('rr.days', JSON.stringify(days)); S.days = {};
})()"""
async def shot(pg, name, full=False):
    await pg.wait_for_timeout(500); await pg.screenshot(path=OUT+name+'.png', full_page=full)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        ctx = await b.new_context(viewport={'width':390,'height':844}, device_scale_factor=2)
        pg = await ctx.new_page(); await pg.route('https://www.gstatic.com/**', lambda r: r.abort())
        await pg.goto('http://localhost:8765/#profile'); await pg.wait_for_timeout(13000)
        await shot(pg, 'profile')
        await pg.fill('#name','Ted'); await pg.fill('#age','39'); await pg.fill('#weight','200'); await pg.click('#pfPersonal button:not([type])'); await pg.wait_for_timeout(3500)
        await pg.evaluate(SEED); await pg.wait_for_timeout(800)
        await pg.evaluate("S.planTab='week'; go('plan')"); await shot(pg, 'plan')
        await pg.evaluate("S.planDay=plan().days[0].weekday; viewPlan()"); await shot(pg, 'day')
        await pg.evaluate("S.planEdit=true; viewPlan()"); await shot(pg, 'day-edit')
        await pg.evaluate("S.planDay=null; S.planEdit=false; viewPlan()"); await pg.click('#wkMenu'); await shot(pg, 'week-menu')
        await pg.evaluate("document.querySelector('.bsheet-wrap')?.remove(); document.body.classList.remove('noscroll'); openWeekWizard(wkKey(0)); S.wiz.step=2; renderWizard()"); await shot(pg, 'wizard')
        await pg.evaluate("closeWizard(); S.planTab='programs'; viewPlan()"); await shot(pg, 'programs')
        await pg.evaluate("startDraft(0); go('workout')"); await shot(pg, 'log-workout')
        await pg.evaluate("S.draft=null; go('nutrition')"); await pg.wait_for_timeout(800); await shot(pg, 'nutrition')
        await pg.evaluate("document.querySelector('#sleepCard').scrollIntoView()"); await shot(pg, 'sleep-fasting')
        await pg.evaluate("openFoodSheet('Snack', todayStr()); S.fs.q='banana'"); await pg.fill('#fsQ','banana'); await pg.wait_for_timeout(1200); await shot(pg, 'food-search')
        await pg.evaluate("closeFoodSheet(); S.calSel=shiftDate(todayStr(),-3); go('log')"); await pg.wait_for_timeout(900); await shot(pg, 'log')
        await pg.evaluate("go('progress')"); await pg.wait_for_timeout(1000); await shot(pg, 'progress')
        await pg.evaluate("document.querySelector('#weightCard').scrollIntoView()"); await shot(pg, 'weight')
        await pg.evaluate("S.mpTab='charts'; go('progress')"); await pg.wait_for_timeout(900)
        await pg.evaluate("document.querySelector('.chartblk')?.scrollIntoView({block:'center'})"); await shot(pg, 'charts')
        await pg.evaluate("""FB = FB || {}; S.user={displayName:'Ted', uid:'x'}; S.chat=[{role:'user',text:'I only have 20 minutes today'},{role:'model',text:'No problem! Do a **20-minute express** version of Full Body A: 2 rounds of goblet squats, push-ups and rows, 45 seconds rest. Want me to swap in a shorter plan for today?', actions:[{type:'swap_exercise',day:0,index:1,to:'push-up',label:'Swap in push-ups',applied:false}]}]; go('coach')"""); await shot(pg, 'coach')
        await pg.evaluate("S.user=null; S.planTab='week'; go('plan')"); await pg.wait_for_timeout(400)
        await pg.evaluate("playWorkout(0)"); await pg.wait_for_timeout(500); await pg.keyboard.press('ArrowRight'); await shot(pg, 'play-phone')
        await pg.set_viewport_size({'width':1280,'height':720}); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(300)
        await pg.screenshot(path=OUT+'play-tv.png')
        await b.close()
asyncio.run(main())
