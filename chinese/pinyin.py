"""Pinyin de frases em chinês por dicionário (segmentação pela palavra mais longa).

Todo caractere usado no conteúdo precisa estar no dicionário: palavras de várias
sílabas resolvem leituras ambíguas (音乐 yīnyuè, 睡觉 shuìjiào, 银行 yínháng).
`pinyin()` levanta erro com os caracteres que faltam, para o build não publicar
pronúncia errada.
"""
from __future__ import annotations

import content as C

# Palavras e caracteres além do vocabulário (partículas, números, palavras dos textos).
EXTRA = {
    # partículas e funções
    "的": "de", "得": "de", "地": "de", "了": "le", "过": "guo", "着": "zhe", "吗": "ma", "呢": "ne", "吧": "ba", "啊": "a",
    "很": "hěn", "太": "tài", "也": "yě", "都": "dōu", "和": "hé", "跟": "gēn", "比": "bǐ", "还": "hái", "还是": "háishi", "或者": "huòzhě",
    "不": "bù", "没": "méi", "没有": "méiyǒu", "就": "jiù", "才": "cái", "再": "zài", "又": "yòu", "只": "zhī", "只要": "zhǐyào", "只有": "zhǐyǒu", "只是": "zhǐshì", "最": "zuì", "非常": "fēicháng",
    "真": "zhēn", "真的": "zhēnde", "一起": "yìqǐ", "一样": "yíyàng", "一点儿": "yìdiǎnr", "一下": "yíxià", "一定": "yídìng", "已经": "yǐjīng",
    "因为": "yīnwèi", "所以": "suǒyǐ", "但是": "dànshì", "可是": "kěshì", "如果": "rúguǒ", "然后": "ránhòu", "先": "xiān", "从": "cóng", "到": "dào",
    "对": "duì", "给": "gěi", "把": "bǎ", "被": "bèi", "向": "xiàng", "往": "wǎng", "离": "lí", "为": "wèi", "为什么": "wèishénme",
    "什么": "shénme", "谁": "shéi", "谁的": "shéi de", "哪": "nǎ", "哪儿": "nǎr", "哪里": "nǎlǐ", "几": "jǐ", "多少": "duōshao", "怎么": "zěnme",
    "怎么样": "zěnmeyàng", "这": "zhè", "那": "nà", "这个": "zhège", "那个": "nàge", "这儿": "zhèr", "那儿": "nàr", "这里": "zhèlǐ", "那里": "nàlǐ",
    "每": "měi", "每天": "měitiān", "些": "xiē", "有点儿": "yǒudiǎnr", "上": "shàng", "下": "xià", "里": "lǐ", "外": "wài", "前": "qián", "后": "hòu",
    "旁边": "pángbiān", "左边": "zuǒbian", "右边": "yòubian", "中间": "zhōngjiān", "以前": "yǐqián", "以后": "yǐhòu", "刚才": "gāngcái", "常常": "chángcháng",
    "从来": "cónglái", "正在": "zhèngzài", "要是": "yàoshi", "她们": "tāmen", "它": "tā", "您": "nín", "你们": "nǐmen", "自己": "zìjǐ", "大家": "dàjiā",
    # números e classificadores
    "一": "yī", "二": "èr", "两": "liǎng", "三": "sān", "四": "sì", "五": "wǔ", "六": "liù", "七": "qī", "八": "bā", "九": "jiǔ", "十": "shí",
    "百": "bǎi", "千": "qiān", "万": "wàn", "〇": "líng", "零": "líng", "半": "bàn", "第": "dì", "号": "hào", "岁": "suì", "块": "kuài", "毛": "máo",
    "元": "yuán", "个": "gè", "本": "běn", "杯": "bēi", "件": "jiàn", "张": "zhāng", "双": "shuāng", "条": "tiáo", "瓶": "píng", "碗": "wǎn",
    "封": "fēng", "部": "bù", "顶": "dǐng", "辆": "liàng", "台": "tái", "位": "wèi", "朵": "duǒ", "首": "shǒu", "次": "cì", "遍": "biàn",
    "分": "fēn", "钟": "zhōng", "星期天": "xīngqītiān", "星期日": "xīngqīrì", "星期一": "xīngqīyī", "星期二": "xīngqī'èr", "星期六": "xīngqīliù",
    "上个": "shàng ge", "下个": "xià ge", "今年": "jīnnián", "明年": "míngnián", "后天": "hòutiān", "前天": "qiántiān",
    # palavras frequentes dos textos e frases
    "名字": "míngzi", "大学": "dàxué", "大学生": "dàxuéshēng", "巴西": "Bāxī", "北京烤鸭": "Běijīng kǎoyā", "烤鸭": "kǎoyā", "下雨": "xiàyǔ", "下雪": "xiàxuě",
    "杂志": "zázhì", "车": "chē", "茶馆": "cháguǎn", "宠物店": "chǒngwùdiàn", "面包店": "miànbāodiàn", "洗手间": "xǐshǒujiān", "烤": "kǎo",
    "客气": "kèqi", "谢谢": "xièxie", "不客气": "bú kèqi", "对不起": "duìbuqǐ", "关系": "guānxi", "没关系": "méi guānxi", "再见": "zàijiàn",
    "请问": "qǐngwèn", "问题": "wèntí", "没问题": "méi wèntí", "好久": "hǎojiǔ", "见": "jiàn", "加油": "jiāyóu", "干杯": "gānbēi", "新年": "xīnnián",
    "晚安": "wǎn'ān", "祝": "zhù", "好运": "hǎoyùn", "好的": "hǎo de", "好听": "hǎotīng", "好看": "hǎokàn", "好玩": "hǎowán", "吃饭": "chīfàn",
    "做饭": "zuòfàn", "看书": "kàn shū", "上课": "shàngkè", "下课": "xiàkè", "下班": "xiàbān", "回家": "huí jiā", "起床": "qǐchuáng",
    "拍照": "pāizhào", "开始": "kāishǐ", "结束": "jiéshù", "觉得": "juéde", "可能": "kěnéng", "应该": "yīnggāi", "需要": "xūyào", "打算": "dǎsuàn",
    "已": "yǐ", "完": "wán", "看完": "kàn wán", "听说": "tīngshuō", "说话": "shuōhuà", "汉语课": "Hànyǔ kè", "课": "kè", "考试": "kǎoshì",
    "作业": "zuòyè", "意思": "yìsi", "有意思": "yǒu yìsi", "时间": "shíjiān", "电话": "diànhuà", "手": "shǒu", "眼睛": "yǎnjing", "身体": "shēntǐ",
    "生病": "shēngbìng", "药": "yào", "休息": "xiūxi", "感冒": "gǎnmào", "发烧": "fāshāo", "头": "tóu", "疼": "téng", "头疼": "tóuténg", "喝水": "hē shuǐ",
    "多喝水": "duō hē shuǐ", "外面": "wàimiàn", "里面": "lǐmiàn", "门": "mén", "窗户": "chuānghu", "颜色": "yánsè", "蓝色": "lánsè", "红色": "hóngsè",
    "黑色": "hēisè", "白色": "báisè", "生活": "shēnghuó", "城市": "chéngshì", "地方": "dìfang", "国家": "guójiā", "世界": "shìjiè", "爱好": "àihào",
    "唱": "chàng", "跳": "tiào", "舞": "wǔ", "队": "duì", "乐队": "yuèduì", "粉丝": "fěnsī", "演": "yǎn", "主角": "zhǔjué", "故事": "gùshi",
    "开心": "kāixīn", "难过": "nánguò", "喜欢": "xǐhuan", "特别": "tèbié", "比较": "bǐjiào", "有名": "yǒumíng", "热闹": "rènao", "安静": "ānjìng",
    "干净": "gānjìng", "舒服": "shūfu", "方便": "fāngbiàn", "重要": "zhòngyào", "清楚": "qīngchu", "简单": "jiǎndān", "认真": "rènzhēn",
    "公斤": "gōngjīn", "春天": "chūntiān", "夏天": "xiàtiān", "秋天": "qiūtiān", "冬天": "dōngtiān", "季节": "jìjié", "暖和": "nuǎnhuo", "凉快": "liángkuai",
    "树": "shù", "叶子": "yèzi", "爬山": "páshān", "海": "hǎi", "海边": "hǎibiān", "坐车": "zuò chē", "开车": "kāichē", "打车": "dǎchē",
    "高铁": "gāotiě", "票价": "piàojià", "小时候": "xiǎo shíhou", "一边": "yìbiān", "已经": "yǐjīng", "房子": "fángzi", "搬家": "bānjiā",
    "附近": "fùjìn", "楼": "lóu", "层": "céng", "邻居": "línjū", "客人": "kèrén", "请客": "qǐngkè", "饿": "è", "渴": "kě", "饱": "bǎo",
    "菜单": "càidān", "点菜": "diǎncài", "米": "mǐ", "辣": "là", "甜": "tián", "酸": "suān", "咸": "xián", "味道": "wèidao", "包子": "bāozi",
    "汤": "tāng", "锅": "guō", "火锅": "huǒguō", "鸡": "jī", "牛肉": "niúròu", "猪肉": "zhūròu", "蔬菜": "shūcài", "最后": "zuìhòu",
    "网上": "wǎngshang", "上网": "shàngwǎng", "网": "wǎng", "快递": "kuàidì", "送": "sòng", "合适": "héshì", "大小": "dàxiǎo", "试": "shì",
    "退": "tuì", "换": "huàn", "商场": "shāngchǎng", "日用品": "rìyòngpǐn", "学期": "xuéqī", "社团": "shètuán", "练习": "liànxí", "表演": "biǎoyǎn",
    "节目": "jiémù", "舞台": "wǔtái", "紧张": "jǐnzhāng", "期待": "qīdài", "学长": "xuézhǎng", "学姐": "xuéjiě", "耐心": "nàixīn", "进步": "jìnbù",
    "地铁站": "dìtiězhàn", "号线": "hào xiàn", "下车": "xià chē", "往前": "wǎng qián", "一直": "yìzhí", "走路": "zǒulù", "左": "zuǒ", "右": "yòu",
    "拐": "guǎi", "左拐": "zuǒ guǎi", "右拐": "yòu guǎi", "故宫": "Gùgōng", "游客": "yóukè", "不用": "búyòng", "谢": "xiè", "愉快": "yúkuài",
    "相机": "xiàngjī", "旧": "jiù", "送给": "sònggěi", "从那以后": "cóng nà yǐhòu", "笑容": "xiàoróng", "展览": "zhǎnlǎn", "办": "bàn",
    "约": "yuē", "约好": "yuē hǎo", "突然": "tūrán", "事": "shì", "有事": "yǒu shì", "晚": "wǎn", "早": "zǎo", "或者": "huòzhě", "怎么办": "zěnme bàn",
    "回复": "huífù", "抱歉": "bàoqiàn", "改": "gǎi", "见面": "jiànmiàn", "中文": "Zhōngwén", "声调": "shēngdiào", "语法": "yǔfǎ", "词": "cí", "背": "bèi",
    "年级": "niánjí", "专业": "zhuānyè", "英语": "Yīngyǔ", "人们": "rénmen", "觉": "jiào", "高": "gāo", "矮": "ǎi", "胖": "pàng", "瘦": "shòu",
    "饭店": "fàndiàn", "早饭": "zǎofàn", "水平": "shuǐpíng", "提高": "tígāo", "机会": "jīhuì", "工资": "gōngzī", "老板": "lǎobǎn", "辛苦": "xīnkǔ",
    "收银": "shōuyín", "整理": "zhěnglǐ", "放假": "fàngjià", "暑假": "shǔjià", "日本": "Rìběn", "攒钱": "zǎn qián", "攒": "zǎn", "老": "lǎo",
    "店": "diàn", "花店": "huādiàn", "厨师": "chúshī", "主人": "zhǔrén", "吵架": "chǎojià", "慢慢": "mànmān", "互相": "hùxiāng", "理解": "lǐjiě",
    "自然": "zìrán", "推荐": "tuījiàn", "部分": "bùfen", "春天的约定": "Chūntiān de yuēdìng", "约定": "yuēdìng", "星光": "Xīngguāng",
    "组合": "zǔhé", "成员": "chéngyuán", "上个月": "shàng ge yuè", "门票": "ménpiào", "荧光棒": "yíngguāngbàng", "挥": "huī", "跟着": "gēnzhe",
    "点": "diǎn", "得很": "de hěn", "热情": "rèqíng", "叫做": "jiàozuò", "做": "zuò", "季": "jì", "雨季": "yǔjì", "七月": "qīyuè", "十月": "shíyuè",
    "极了": "jí le", "开": "kāi", "颜": "yán", "红叶": "hóngyè", "很多": "hěn duō", "人多": "rén duō", "下午茶": "xiàwǔchá", "冰": "bīng",
    "冰美式": "bīng měishì", "美式": "měishì", "大杯": "dà bēi", "中杯": "zhōng bēi", "欢迎": "huānyíng", "光临": "guānglín", "欢迎光临": "huānyíng guānglín",
    "要": "yào", "给你": "gěi nǐ", "这是": "zhè shì", "收": "shōu", "店员": "diànyuán", "顾客": "gùkè", "顾": "gù", "元钱": "yuán qián", "价格": "jiàgé",
    "缺点": "quēdiǎn", "优点": "yōudiǎn", "鞋子": "xiézi", "穿上": "chuān shàng", "合": "hé", "适": "shì", "其他": "qítā", "东西": "dōngxi",
    "交": "jiāo", "交通": "jiāotōng", "离开": "líkāi", "到达": "dàodá", "出发": "chūfā", "周": "zhōu", "两次": "liǎng cì", "星期二和星期四": "xīngqī'èr hé xīngqīsì",
    "星期四": "xīngqīsì", "跳舞": "tiàowǔ", "舞蹈": "wǔdǎo", "动作": "dòngzuò", "大学的": "dàxué de", "以前的": "yǐqián de",
    "王明": "Wáng Míng", "小美": "Xiǎoměi", "儿": "ér", "一会儿": "yíhuìr", "外滩": "Wàitān", "夜景": "yèjǐng", "小笼包": "xiǎolóngbāo",
    "礼物": "lǐwù", "天": "tiān", "晴天": "qíngtiān", "出门": "chūmén", "带": "dài", "带着": "dàizhe", "雨伞": "yǔsǎn", "面": "miàn",
    "牛肉面": "niúròumiàn", "而且": "érqiě", "下次": "xiàcì", "更": "gèng", "亮": "liàng", "让": "ràng", "好好": "hǎohǎo",
    "便利店": "biànlìdiàn", "打工": "dǎgōng", "起来": "qǐlái", "发生": "fāshēng", "最近": "zuìjìn", "看看": "kànkan", "看到": "kàndào",
    "后来": "hòulái", "天安门": "Tiān'ānmén", "东": "dōng", "站": "zhàn", "路人": "lùrén", "左右": "zuǒyòu", "高中": "gāozhōng",
    "摄影展": "shèyǐngzhǎn", "北方": "běifāng", "蓝": "lán", "中": "zhōng", "美": "měi", "到不了": "dào bu liǎo", "购物": "gòuwù",
    "送到": "sòngdào", "有时候": "yǒu shíhou", "参加": "cānjiā", "节日": "jiérì", "担心": "dānxīn", "教": "jiāo", "上台": "shàngtái",
    "第一次": "dì-yī cì", "好吃的": "hǎochī de",
    "跑": "pǎo", "片": "piàn", "份": "fèn", "月份": "yuèfèn", "拍照片": "pāi zhàopiàn",
}

# Palavras de vários caracteres do conteúdo + EXTRA formam o dicionário.
DICT: dict[str, str] = {}
for hz, py, *_ in C.VOCAB:
    DICT[hz] = py
for hz, py, *_ in C.PHRASES:
    DICT.setdefault(hz.rstrip("？！。……"), py)
DICT.update({k: v for k, v in EXTRA.items() if k not in DICT})
MAXLEN = max(len(k) for k in DICT)
PUNCT = {"。": ".", "，": ",", "？": "?", "！": "!", "、": ",", "：": ":", "；": ";", "“": "“", "”": "”", "（": "(", "）": ")", "…": "…", "—": "—", "《": "«", "》": "»"}


def is_hanzi(ch: str) -> bool:
    return "一" <= ch <= "鿿" or ch == "〇"


def pinyin(text: str) -> str:
    """Pinyin por palavra, separado por espaço; pontuação convertida."""
    out, missing, i = [], [], 0
    while i < len(text):
        ch = text[i]
        if not is_hanzi(ch):
            if ch in PUNCT:
                if out:
                    out[-1] += PUNCT[ch]
            elif ch.strip():
                out.append(ch)
            i += 1
            continue
        for size in range(min(MAXLEN, len(text) - i), 0, -1):
            word = text[i:i + size]
            if word in DICT:
                out.append(DICT[word])
                i += size
                break
        else:
            missing.append(ch)
            i += 1
    if missing:
        raise KeyError(f"Sem pinyin para: {''.join(dict.fromkeys(missing))} (em “{text}”)")
    return " ".join(out).replace(" …", "…")
