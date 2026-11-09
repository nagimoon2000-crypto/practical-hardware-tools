(()=>{
const id='G-JMKNEEYS39',key='pht-analytics-choice-v1';
let enabled=false,started=false;
const status=document.getElementById('analytics-status');
function tag(){window.dataLayer=window.dataLayer||[];window.dataLayer.push(arguments)}
function enable(){
 enabled=true;window['ga-disable-'+id]=false;
 if(!started){
  started=true;
  tag('consent','default',{analytics_storage:'granted',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
  tag('js',new Date());
  const clean=new URL(location.origin+location.pathname);
  const query=new URLSearchParams(location.search);
  for(const k of ['utm_source','utm_medium','utm_campaign']){
   const v=query.get(k);if(v&&/^[a-zA-Z0-9_-]{1,80}$/.test(v))clean.searchParams.set(k,v);
  }
  let ref='';try{ref=new URL(document.referrer).origin}catch{}
  tag('config',id,{page_location:clean.href,page_referrer:ref,allow_google_signals:false,allow_ad_personalization_signals:false});
  const script=document.createElement('script');script.async=true;script.src='https://www.googletagmanager.com/gtag/js?id='+id;document.head.append(script);
 }else tag('consent','update',{analytics_storage:'granted'});
 status.textContent='Optional analytics: allowed.';
}
function choose(yes){
 try{localStorage.setItem(key,yes?'yes':'no')}catch{}
 if(yes)enable();else{
  enabled=false;window['ga-disable-'+id]=true;
  if(started)tag('consent','update',{analytics_storage:'denied'});
  status.textContent='Optional analytics: off. All tools remain available.';
 }
}
document.getElementById('analytics-yes').addEventListener('click',()=>choose(true));
document.getElementById('analytics-no').addEventListener('click',()=>choose(false));
let saved;try{saved=localStorage.getItem(key)}catch{}
if(saved==='yes')enable();else status.textContent=saved==='no'?'Optional analytics: off.':'Analytics stays off until you allow it.';
const canonical = document.querySelector('link[rel="canonical"]');
const pagePlacement = canonical
 ? new URL(canonical.href).pathname.split('/').filter(Boolean).pop()
 : 'existing_link';
const used=new Set();
const paidIds = new Set(["mfpHk", "zog3I", "Cp6Rs", "UEoMx", "5GwqN", "JYv97", "2fX4i", "ItqCe", "bOsai", "93hu7", "iMlGT", "tnLMh", "GMWBE", "beH47", "NubRV", "1EQNl", "WT3eb", "QsGuA", "adpO3", "MtxAU", "mKYNV", "yeLKj", "R9fSO", "r5X3U", "owIUE", "SYC3D", "lgSGa", "X8eSk", "YAXRH", "s9ud4", "nG12C", "rqxF5", "kT5sy", "ZeNBd", "4YRf2", "VoJaw", "pXqe5", "9n0zw", "5XZRN", "W8bM0", "W6iUt", "8Mtc0", "5XeO9", "bNX7Z", "oqhaZ", "nrIe9", "nsKmD", "mLiMD", "rGOe1", "d6XgE", "6yfUg", "OVoy5", "DF3Sl", "DgP4z", "2ZpLy", "eYw9a", "fAjhO", "Y4dKU", "JcDFr", "9PVDO", "bcfR4", "qacOQ", "B0Hgr", "o2uVc", "B1lPG", "JdmYg", "2qdal", "KWTAX", "9GtFr", "qKy5d", "HFVvu", "ZmOby", "HciOw", "UHrRu", "cDmEe", "61VPi", "ZSwCX", "6BClq", "Vp0yU", "tHsub", "ZgRsj", "U0QzT", "zEJmZ", "KdH0k"]);
function recordResult(calculator) {
 if (enabled) tag('event','calculator_result',{calculator});
}
document.addEventListener('submit', event => {
 const form = event.target;
 if (!enabled || !event.isTrusted || form.id !== 'exercise') return;
 const product = form.dataset.product;
 if (!paidIds.has(product) || !form.checkValidity() || used.has(product)) return;
 used.add(product);
 tag('event','practice_answer_checked',{product_id:product,placement:pagePlacement});
});
document.addEventListener('input', event => {
 const form = event.target.closest('form[data-kind]');
 if (event.isTrusted && form && form.querySelector('.result:not(.invalid)')) recordResult(form.dataset.kind);
});
document.addEventListener('click', event => {
 if (!enabled || !event.isTrusted) return;
 const preset = event.target.closest('.try-scenario');
 if (preset) {
  const form = document.querySelector('form[data-kind="' + preset.dataset.tool + '"]');
  if (form && form.querySelector('.result:not(.invalid)')) recordResult(form.dataset.kind);
 }
 const link = event.target.closest('a[href]');
 if (!link) return;
 const url = new URL(link.href);
 const match = /^\/b\/([A-Za-z0-9]+)\/?$/.exec(url.pathname);
 if (url.origin === 'https://payhip.com' && match && paidIds.has(match[1]))
  tag('event','paid_product_link_click',{product_id:match[1],placement:link.dataset.placement || pagePlacement});
});

document.addEventListener('pht:retention-use',()=>{recordResult('storage_retention');if(!enabled||used.has('storage_retention'))return;used.add('storage_retention');tag('event','calculator_use',{calculator:'storage_retention'});});
document.addEventListener('pht:i2c-use',()=>{
 recordResult('i2c');if(!enabled||used.has('i2c'))return;
 used.add('i2c');tag('event','calculator_use',{calculator:'i2c'});
});
document.addEventListener('pht:i2c-download',()=>{
 if(enabled)tag('event','file_download',{file_extension:'csv',calculator:'i2c'});
});
document.addEventListener('pht:link-copied',()=>{
 if(enabled)tag('event','share',{method:'copy_link',content_type:'hardware_resource'});
});
document.addEventListener('change',e=>{
 const form=e.target.closest('form[data-kind]');if(!enabled||!form||used.has(form.dataset.kind))return;
 used.add(form.dataset.kind);tag('event','calculator_use',{calculator:form.dataset.kind});
});
document.addEventListener('click',e=>{
 if(!enabled)return;
 const download=e.target.closest('.download');
 if(download&&!download.closest('form').querySelector('.invalid'))tag('event','file_download',{file_extension:'csv',calculator:download.closest('form').dataset.kind});
 const link=e.target.closest('a[href]');if(!link)return;
 const url=new URL(link.href);
 if(url.hostname==='payhip.com'){
  if(/^\/b\/[A-Za-z0-9]+\/?$/.test(url.pathname))tag('event','product_click',{product_path:url.pathname});
  else if(url.pathname.includes('/blog/'))tag('event','guide_click',{guide_path:url.pathname});
 }
});
})();
