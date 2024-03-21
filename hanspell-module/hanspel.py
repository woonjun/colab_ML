import pandas as pd
data = pd.read_excel("C:/Users/82107/Documents/GitHub/hello/py-hanspell-master/google.xlsx")
data.dropna(subset=['review-full-text'], inplace=True)
data['result'] = 1
data = data.iloc[:,2:]
data2 = pd.read_excel("C:/Users/82107/Documents/GitHub/hello/py-hanspell-master/ai_review.xlsx")
reviews = [
    "성심당의 빵은 정말 맛있습니다. 부드럽고 달콤한 맛이 일품이에요.",
    "크림이 풍부해서 한 입 먹을 때마다 행복한 느낌이 들어요.",
    "다양한 종류의 빵이 있어서 매번 새로운 맛을 즐길 수 있어 좋아요.",
    "가격 대비 양이 많아서 가족과 함께 나눠 먹기에 딱이에요.",
    "성심당의 케이크는 생일 파티에 딱이에요. 다양한 디자인도 매력적이에요.",
    "초코렛 크로와상은 정말 까먹을 수 없는 맛이에요. 강추합니다.",
    "좌석이 편안해서 친구들과 잠시 쉬면서 디저트를 즐길 수 있어 좋아요.",
    "도넛의 바삭한 식감이 일품이에요. 커피와 함께 먹으면 최고입니다.",
    "가게 분위기도 아늑하고 깔끔해서 자주 방문하게 되는 곳이에요.",
    "피스타치오 크림빵은 정말 고소하고 입맛 돋우는 맛이에요.",
    "다쿠아즈는 바삭한 겉면과 부드러운 속이 조화롭게 어우러져 맛있어요.",
    "친절한 직원들이 있어서 더 기분 좋게 구매할 수 있어요.",
    "단호박 호두파이는 달콤함과 고소함이 조화롭게 어울려 맛있어요.",
    "성심당의 빵은 신선하고 질이 좋아서 항상 신났어요.",
    "디저트 마니아라면 꼭 가봐야 할 곳 중 하나에요.",
    "가게 내부가 깔끔하게 정리되어 있어서 좋아요.",
    "이색적인 토핑이 있는 크로와상은 정말 독특한 맛이에요.",
    "커피 메뉴도 다양해서 커피 좋아하는 사람들에게 추천합니다.",
    "매장 위치가 편리해서 자주 들리게 되는 곳이에요.",
    "프로푸드에서 인정받은 맛집 중 하나라고 생각해요."
]

new_reviews_df = pd.DataFrame(reviews, columns=['review-full-text'])
new_reviews_df['result'] = 0
combined_df = pd.concat([data, new_reviews_df], ignore_index=True)
combined_df.rename(columns={'review-full-text': 'text', 'result': 'label'}, inplace=True)

combined_df = pd.concat([combined_df, data2], ignore_index=True)

import pandas as pd
from hanspell import spell_checker
from tqdm import tqdm
train = combined_df

results = []

for i in tqdm(range(len(train))):

    try:
        intext = train['text'][i]
        hanspell_sent = spell_checker.check(intext)
        CHECKED = hanspell_sent.as_dict()
        results.append(CHECKED['errors'])
    except:
        results.append("unknown")
train['result'] = results
train.to_csv("./train_맞춤법검사.csv", index=False, encoding="utf-8-sig")
train