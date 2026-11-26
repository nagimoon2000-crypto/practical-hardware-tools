"""Render the public free-exercise hub using verified Payhip products."""
from pathlib import Path
from html import escape as e
import json

SLUG='ai-workflow-practice-ko'
TITLE='AI 업무 활용법 10가지: 무료 예제로 먼저 검수해 보세요'
DESCRIPTION='영수증 정리, 설문 분석, 견적 비교, 번역 검수부터 면접과 FAQ까지. 무료 문제와 해설을 먼저 풀고 필요한 한국어 실습 워크북을 선택하세요.'
ORIGIN='https://nagimoon2000-crypto.github.io/practical-hardware-tools/'

def render(analytics):
 data=json.loads(Path(__file__).with_name('ai-workflows-data.json').read_text(encoding='utf8'))
 blocks=[]
 for t in data:
  c=t['case'];pid=t['id'];slug=t['slug']
  url=f'https://payhip.com/b/{pid}?utm_source=hardware_tools&amp;utm_medium=free_example&amp;utm_campaign=ai_workflows_20261125'
  blocks.append(f'''<article id="{slug}"><h2>{e(t['title'])}</h2><p>{e(t['outcome'])}</p><h3>무료 실습: {e(c['name'])}</h3><p>{e(c['input'])}</p><p>먼저 자신의 답과 확인할 조건을 적어 보세요. 아래 해설은 가상 사례의 정답이며 실제 고객 성과가 아닙니다.</p><details data-workflow="{slug}"><summary>해설과 흔한 오류 보기</summary><p>{e(c['answer'])}</p><p><strong>오류 점검:</strong> {e(c['trap'])}</p></details><p>{e(t['boundary'])}</p><p><a class="cta" data-placement="ai_workflow_{slug}" href="{url}">예외 사례·실무양식 확인하기 · US$12</a></p><p class="small">상품 페이지 Preview에서 무료 TXT도 확인할 수 있습니다. 전체판: 독립 사례3개·해설·요청문5개·실무양식·검수표, 한국어 TXT 7개 ZIP.</p></article>''')
 chooser='<section id="choose"><h2>업무 하나만 골라 무료로 시작하세요</h2><p>아래에서 지금 필요한 결과를 선택하면 해당 문제로 이동합니다. 가입이나 AI 이용권 구매는 필요하지 않습니다.</p><div class="choices"><a href="#expense-evidence">지출 합계가 안 맞아요 → 중복·환불 점검</a><a href="#survey-coding">설문 의견을 요약해야 해요 → 분류·빈도 검산</a><a href="#translation-qa">번역을 믿어도 될까요? → 숫자·부정 검수</a><a href="#sop-handover">인수인계가 막막해요 → 절차·예외 정리</a></div><details><summary>다른 업무 6개 보기</summary><ul>PLACEHOLDER</ul></details></section>'
 chooser=chooser.replace('PLACEHOLDER',''.join(f'<li><a href="#{x["slug"]}">{e(x["title"])}</a></li>' for x in data if x['slug'] not in ['expense-evidence','survey-coding','translation-qa','sop-handover']))
 offer='<section id="contents"><h2>무료 예제와 전체판의 차이</h2><p><strong>무료:</strong> 이 페이지에서 주제별 문제 1개, 정답과 흔한 오류를 바로 확인합니다.</p><p><strong>전체판 · 주제당 US$12:</strong> 독립 사례 3개와 해설, 요청문 5개, 반복 사용 양식·검수표, 시작 안내·라이선스가 한국어 TXT 7개 ZIP에 포함됩니다.</p><p>PDF·영상 강의·자동 실행 프로그램·AI 이용권은 포함하지 않습니다. 먼저 무료 예제를 읽고 실제 업무에 맞는 주제 하나만 선택하세요.</p><details><summary>구매 전에 무엇을 확인하나요?</summary><p>상품 페이지의 Preview에서 무료 TXT를 확인하세요. ZIP 압축을 풀고 UTF-8 텍스트를 읽을 수 있는 환경이 필요합니다. 실제 업무 자료는 민감정보를 제거한 뒤 사용하세요. AI 답변은 반드시 원본과 대조해야 합니다.</p></details><details><summary>AI 서비스 유료 구독이 필요한가요?</summary><p>학습 자료는 AI 서비스 없이도 읽을 수 있습니다. 요청문을 실행하려면 사용하는 AI 서비스의 계정과 해당 기능이 필요하며 이용 조건은 서비스마다 다릅니다. 구매 가격에 AI 사용료는 포함되지 않습니다.</p></details></section>'
 links=''.join(f'<li><a href="#{x["slug"]}">{e(x["title"])}</a></li>' for x in data)
 return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(TITLE)} | Practical Hardware Tools</title><meta name="description" content="{e(DESCRIPTION)}"><meta name="google-site-verification" content="751gEk6PZGH4V62ORHZoDlfiI__NPh7NxvHbU6bn61E" /><link rel="canonical" href="{ORIGIN+SLUG}/"><meta property="og:title" content="{e(TITLE)}"><meta property="og:description" content="{e(DESCRIPTION)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN+SLUG}/"><style>*{{box-sizing:border-box}}body{{margin:0;background:#f3f5f1;color:#18343b;font:17px/1.8 system-ui,sans-serif}}main,nav{{max-width:900px;margin:auto;padding:24px}}header,article,section{{background:white;padding:28px;border-radius:16px;margin:20px 0}}header{{background:#183f49;color:white}}h1{{font-size:clamp(27px,5vw,42px);line-height:1.3}}h2{{line-height:1.4}}a{{color:#125c69}}header a{{color:white}}.cta{{display:inline-block;background:#183f49;color:white;padding:12px 18px;border-radius:8px}}.choices{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px}}.choices a{{padding:16px;border:1px solid #b6c9c8;border-radius:8px;text-decoration:none}}article{{scroll-margin-top:20px}}details{{padding:16px;background:#edf4ef}}summary{{cursor:pointer;font-weight:bold}}.small{{font-size:14px}}button{{font:inherit;padding:10px;margin:6px}}a:focus-visible,summary:focus-visible,button:focus-visible{{outline:3px solid #e29322;outline-offset:3px}}</style></head><body><nav><a href="../">무료 하드웨어 계산기</a> · <a href="../hardware-spreadsheet-guides/">전체 다운로드 상품</a></nav><main><header><p>MOONSFACTORY · 무료 실습</p><h1>{e(TITLE)}</h1><p>AI 답변을 바로 쓰기 전에 원본과 대조하는 연습입니다. 로그인·다운로드 없이 예제를 읽고, 필요한 주제만 선택하세요.</p></header>{chooser}{offer}{''.join(blocks)}<section><h2>숫자가 들어간 답은 따로 검산하세요</h2><p>하드웨어 업무라면 <a href="../i2c-pullup-resistor-calculator/">I²C 저항 계산기</a>와 <a href="../supercapacitor-hold-up-calculator/">슈퍼커패시터 계산기</a>에서 가정과 단위를 먼저 확인하세요. 이 도구는 위 업무용 금액 계산을 대신하지 않습니다.</p><p>주제 선정 참고: 2026-11-25 구글·네이버에서 ChatGPT, Gemini, Claude, NotebookLM, Perplexity를 비교했습니다. 위 목록은 실무 주제 10개이며 전체 검색순위 1~10위나 검증된 구매 수요를 뜻하지 않습니다.</p></section></main>{analytics.replace('ASSET_ROOT','../')}</body></html>'''

def install(out,analytics):
 out=Path(out);dest=out/SLUG;dest.mkdir(exist_ok=True)
 (dest/'index.html').write_text(render(analytics),encoding='utf8')
 for rel,prefix in [('index.html',''),('hardware-spreadsheet-guides/index.html','../')]:
  p=out/rel;s=p.read_text(encoding='utf8')
  if 'id="ai-workflows-entry"' not in s:
   s=s.replace('</main>',f'<section id="ai-workflows-entry" lang="ko"><h2>AI 업무 활용 무료 실습 10가지</h2><p>영수증·설문·견적·번역·면접의 오류를 직접 찾아보세요.</p><a href="{prefix}{SLUG}/">무료 문제와 해설 먼저 보기</a></section></main>')
  p.write_text(s,encoding='utf8')

if __name__ == '__main__':
 import sys
 if len(sys.argv)!=3: raise SystemExit('Usage: python ai_workflows.py OUTPUT_DIRECTORY ANALYTICS_MARKUP_FILE')
 install(Path(sys.argv[1]),Path(sys.argv[2]).read_text(encoding='utf8'))
