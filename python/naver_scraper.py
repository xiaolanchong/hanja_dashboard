# -*- coding: utf-8 -*-

import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

grade8_1 = '校敎九國軍釒金南女年大東六萬母木門民北白父四山三生西先小水室十女五王外月六二人日一長弟中靑寸七土八學韓兄火家間江車空工記氣男內農答動力立每名物方不事上姓世手時市食安力午右立自子場電前全正足左直車平下漢海話活孝後歌口旗來老洞同冬登來老里林面命文問百便夫數算色夕所少數植心語然有育邑里林入字祖住主重紙地川天千草村秋春出洞便夏花休角各計界高功共公科果光球今急樂短堂對代圖讀童讀等樂理利明聞班反半發放部分省書線雪省消術始神身神新信樂藥弱業樂用勇飮音意利理昨作才戰庭第題注集窓淸表風幸現形和會感強開京苦古交區郡近根級路綠多待度頭禮例路綠李目美米朴番別病服本死使石席速孫樹習勝式失愛野夜陽洋訁言永英禮例溫遠園由油銀醫衣李者章在定朝族晝親度太通特合行行向號畫黃訓價客格見結決敬告課關觀舊具局己基朗念勞能團當宅德到獨朗良旅歷練勞類流陸望法變兵福福奉士史仕産參相商鮮仙說性說洗歲束首宿順識臣實兒惡約養良旅歷練說念惡要雨友雲元偉類流陸以任財材的展典傳切店情調卒種週州識知質參責切充宅品筆必害見化效凶可加改擧去建健件輕競景考固曲橋救貴規給汽期技吉落冷壇談都島落冷量領令料馬末亡賣買無倍鼻費比氷査思寫賞序選船善葉示案量魚漁億熱葉令領屋完曜料浴牜牛雄願院原位耳因災再爭貯赤停操終罪止唱鐵初最祝致則打他卓炭板敗河寒許湖患黑街假監減講康個檢缺潔警經慶境係故官究求句宮權句極禁起器羅難暖怒努錄論端檀斷單達擔黨隊帶導督毒銅豆斗得燈羅兩麗連列怒錄論留律滿脈毛牧武務未味密博防訪房配背拜罰伐壁邊步寶報保復復府富婦副佛飛非悲備貧謝舍師寺殺狀想床常設誠聲聖盛星城細稅勢素笑掃續俗送殺收授守受修純承詩試視是施息申深眼暗壓液羊兩如麗餘逆連硏煙演列榮藝誤玉往謠容圓員爲衛留肉律恩陰應議義移益益認引印障狀將低敵田絶接精政精程製祭濟提制際除鳥造早助尊宗走竹準衆增至支指志職進眞次察創處請銃總蓄築蟲忠取測齒置治侵快態統退破波砲暴布包暴票豊限航港解香鄕虛驗賢血協惠護戶好呼貨確回吸興希暇覺刻簡看干甘敢甲降更據拒巨居傑儉激擊犬堅驚鏡更傾鷄階繼系戒季庫孤穀困骨攻孔管鑛構群君屈窮卷勸券歸均劇筋勤紀機寄奇卵亂納段逃盜徒卵亂覽略糧慮烈龍柳輪離異妹勉鳴模妙墓舞拍髮妨範犯辯普複伏負否粉憤祕碑批辭絲私射散象傷宣舌屬損頌松秀肅叔崇氏額略糧樣嚴與易域鉛緣燃延烈映迎營豫龍郵遇優源援怨慰威委圍危遺遊柳儒乳輪隱疑儀依易離異仁資姿姉殘雜獎裝腸張帳壯底適賊績籍積錢轉專折點占整丁靜帝組潮條存鍾從座酒朱周證誌智持織陣盡珍差讚採冊泉聽廳招推縮趣就層針寢稱歎彈脫探擇討痛鬪投派判篇評閉胞爆標避疲閑恨降抗核憲險革顯刑或混婚紅華環歡況灰厚候揮喜架佳閣脚肝懇幹刊鑑鋼綱剛蓋槪介距乾劍隔訣謙兼頃耕硬徑溪械桂契啓鼓稿姑谷哭貢恭恐供誇寡館館貫慣寬冠狂怪壞較巧拘久丘菊弓拳鬼菌克契錦禽琴及騎祈畿其企緊諾蘭欄浪廊娘耐寧露爐奴祿弄雷腦累漏樓陵泥茶旦但丹淡踏糖唐貸臺陶途渡桃刀倒突凍絡諾蘭欄丹郞浪廊涼梁勵曆鍊蓮聯戀裂靈嶺寧露爐祿弄雷賴累漏樓倫率栗隆陵裏履吏臨麻磨莫漠幕晩妄梅媒麥盟盲猛孟綿眠免滅銘貌謀慕睦沒蒙夢貿茂默墨紋勿微尾迫薄飯飯般盤拔芳輩排培伯繁凡碧丙譜補覆腹鳳逢峯封賦腐簿符浮扶付附紛奮奔拂肥婢妃卑邪詞蛇祀沙斜司索削森霜詳裳桑尙喪償像塞索塞署緖恕徐釋惜禪旋訴蘇疏燒率訟鎖刷衰需隨輸獸殊愁帥壽垂熟淑瞬旬巡述襲拾濕昇僧乘侍飾辰愼甚沈審拾雙雅阿芽牙我亞顔岸巖央仰哀若若讓梁揚壤御抑憶勵驛譯疫曆役亦鍊蓮軟聯燕沿戀宴裂悅鹽炎染影嶺寧靈譽烏悟獄瓦緩辱欲慾羽羽憂愚宇偶韻越僞謂胃誘裕維猶柔悠幽幼潤倫率栗隆乙淫已履吏裏泥翼忍逸逸賃臨壬紫慈刺潛暫藏葬莊臟粧掌丈載裁栽著抵蹟跡笛摘寂殿漸頂淨征廷亭井貞諸諸齊租照兆縱坐鑄珠洲株柱宙奏仲卽蒸症曾憎池枝之震陳鎭辰振秩疾執徵茶此借錯贊蒼昌倉菜彩債策妻拓戚尺刺遷踐賤淺徹哲滯超肖礎觸促催追畜衝醉吹側稚恥値漆浸沈拓奪塔糖湯泰殆澤兔吐透版片偏編肺弊廢浦捕楓被皮彼畢賀荷何鶴鶴汗割陷含項恒響獻玄懸穴脅衡慧豪虎胡浩惑魂忽洪禍還換荒皇懷悔獲劃橫胸戲稀却姦渴豈皆慨乞遣肩絹牽竟庚卿繫癸顧枯坤郭掛愧塊郊矯龜驅苟狗懼俱厥軌龜糾叫龜謹斤僅肯飢豈欺棄旣忌幾那奈濫奈乃鹿惱淚屢畓跳稻挑塗篤豚敦鈍屯騰濫掠諒憐劣廉獵零隷鹿僚了淚屢梨隣漫慢茫罔忙忘埋冥某暮募冒侮苗廟卯霧戊迷眉敏憫蜜泊返叛伴邦傍倣杯飜煩辨竝屛卜蜂赴墳朋崩頻賓聘賜詐斯捨巳似朔祥祥嘗逝誓暑敍庶析昔涉攝騷蔬昭召粟誦須雖遂誰睡搜囚孰脣殉循戌矢辛晨伸尋餓岳雁謁押殃涯厄耶也躍掠諒楊於焉汝余予輿憐閱劣廉獵泳零詠隸銳汚娛嗚吾傲翁擁臥曰畏遙腰搖僚了庸尤又于云違緯酉愈惟唯閏吟泣凝矣宜夷而梨隣寅姻玆恣酌爵墻宰哉滴竊蝶訂堤燥弔拙佐舟遵俊贈遲只姪懲且捉慙慘暢斥薦添尖妾晴遞逮替秒抄燭聰醜抽逐丑臭枕妥墮濯濁托誕貪怠頗罷播把販貝遍蔽幣飽抱幅漂匹旱咸巷該奚亥享軒縣絃嫌螢亨兮毫互乎昏鴻弘禾擴穫丸曉侯毁輝携迦軻賈柯伽珏艮杆鞨葛邯憾鉀岬疆彊崗岡姜塏价坑鍵桀杰揭憩甄瓊璟炅儆雇賈皐滑串菓瓜戈琯款串槐傀膠絞僑鷗邱購玖歐鞠窟掘圈闕閨珪揆奎圭瑾槿兢麒驥騏耆箕璣琪琦淇沂棋岐冀裸洛爛藍拉鷺魯蘆盧籠濃尿尼溺鍛湍膽潭塘戴垈悳燾悼頓燉惇乭董棟桐杜鄧謄藤裸洛爛藍拉萊輛樑亮驪礪廬呂煉漣濂玲醴鷺魯蘆盧籠遼療謬硫劉崙楞麟魔痲摩膜蠻灣娩靺網魅枚貊覓俛沔冕蔑謨茅矛牟帽穆沐昴紊汶彌閔珉玟旼旻舶磻潘搬鉢渤龐紡旁賠裵俳柏磻閥筏范汎僻弁卞秉炳柄昺昞倂輔甫潽馥蓬縫俸膚敷傅阜釜芬弗鵬泌毘毖匪丕彬飼飼赦泗唆酸傘蔘揷箱庠舒瑞錫碩晳奭繕璿璇瑄薛卨陝蟾纖暹燮晟貰邵紹沼巢宋隋銖洙荀舜盾珣淳洵瑟繩升柴屍軾湜殖腎紳瀋握閼癌鴨礙艾埃惹倻襄孃亮彦廬呂驪礪衍硯煉漣淵姸閻厭燁暎盈瑩瑛玲預醴芮睿濊梧墺吳鈺沃穩雍邕甕莞汪旺歪倭遼耀療尿姚妖堯鏞鎔瑢熔溶傭禹祐佑頊郁煜昱旭芸鬱蔚熊袁苑瑗媛渭尉魏韋踰硫楡庾劉兪鈗胤崙尹允融誾殷垠鷹怡伊貳珥翊溺麟刃鎰壹佾妊雌諮磁滋蠶蔣璋獐庄沮甸鼎珽汀楨晶旌呈偵鄭艇禎劑釣趙祚曺措彫綜琮駐疇駿濬浚晙峻埈准芝脂旨址稷稙診秦津晋塵窒輯遮餐鑽瓚璨燦札刹斬滄昶敞彰采蔡埰悽隻陟釧澈撤喆瞻諜締焦楚哨蜀崔鄒趨楸軸蹴椿衷沖聚炊雉峙託琢灘耽颱胎台兌坡阪霸彭扁坪鮑鋪葡抛怖杓馮泌弼虐翰艦陜沆亢杏赫爀鉉炫弦峴峽馨邢瑩炯瀅型鎬祜皓濠澔晧昊扈壕酷泓靴樺嬅煥桓幻滑滉晃淮檜廻喉后壎勳薰熏徽烋匈欽羲禧熹熙憙嬉姬噫駕袈苛稼嫁嘉哥呵殼恪諫艱竿癎澗揀奸墾褐竭喝紺瞰疳柑堪勘閘匣薑腔糠慷芥箇漑愾凱羹醵渠倨虔腱巾怯劫偈覡膈檄鵑譴繭鯨頸莖脛磬痙梗憬勁悸錮辜袴膏股痼敲拷呱叩鵠梏袞棍昆汨鞏拱顆藿槨廓顴灌棺括刮胱曠壙匡罫卦魁拐乖轟肱宏驕轎蛟皎狡攪嬌喬咬廏鳩駒鉤軀謳衢舅臼矩灸溝毆柩枸嶇寇垢嘔仇窘躬穹眷捲倦蹶几詭潰櫃机逵葵窺硅橘隙棘戟剋饉覲襟衾擒汲扱矜亘譏肌羈綺畸杞朞崎妓嗜伎拮喫邏螺癩拿拏懶懦儺駱酪烙鸞煖捺捏衲蠟臘囊狼撚駑虜擄弩碌膿聾壟賂磊牢壘陋訥紐肋勒凜菱綾稜凌匿蛋緞簞疸撻譚痰澹曇憺遝螳棠撞袋擡鍍蹈賭萄禱睹濤滔淘搗掉屠堵禿瀆沌胴瞳疼憧痘兜遁臀橙邏螺癩拏懶烙駱酪鸞瀾辣剌籃蠟臘狼粱倆黎閭濾戾侶礫瀝輦簾殮斂齡鈴逞囹虜擄撈麓碌聾瓏壟賂磊牢儡聊瞭燎寮陋壘瘤琉溜戮綸淪慄肋勒凜菱綾稜凌釐裡罹籬痢悧俚鱗躪燐吝淋粒笠寞鰻饅輓蔓瞞挽彎卍襪沫抹惘芒呆邁罵煤昧寐萌麪緬眄棉酩螟皿溟暝袂糢耗牡摸歿猫渺杳描誣蕪畝毋撫拇憮巫蚊靡薇媚悶謐樸撲搏剝駁膊縛粕箔珀頒蟠絆礬畔槃斑攀拌魃醱跋潑撥勃謗膀肪榜枋昉彷幇尨坊陪胚湃徘魄帛藩蕃泛氾梵帆闢癖璧擘劈鼈瞥餠甁菩洑堡鰒輻匐僕鋒烽棒捧賻訃芙腑斧孵埠咐剖俯駙雰糞盆焚扮忿噴吩彿繃硼棚妣鄙譬誹裨蜚臂脾翡緋秕砒痺琵沸扉憊庇匕瀕濱殯嬪嚬憑麝蓑紗祠獅瀉徙娑奢嗣些疝珊刪薩煞撒滲澁觴翔爽孀璽嗇甥牲鼠黍薯胥犀棲曙抒嶼壻潟銑膳腺羨煽扇渫洩泄屑閃殲醒遡逍蕭簫瘙疎甦梳搔宵塑贖遜悚碎灑讎髓酬袖蒐羞繡粹竪穗瘦狩戍嫂菽夙塾馴醇筍膝丞柿豺諡猜弑媤匙蝕熄拭迅訊蜃薪燼宸娠呻悉什訝衙啞俄顎愕堊鞍晏按軋斡闇庵昂鴦秧怏靄隘曖崖腋縊扼鶯櫻爺揶冶葯癢釀瘍攘恙禦瘀圄臆諺堰掩奄儼濾黎閭繹鳶輦筵椽撚捐涅咽簾艶焰殮嬰囹鈴詣裔穢曳懊寤奧伍蘊壅訛蝸渦頑阮腕玩宛婉枉矮猥巍饒邀窯窈燎擾撓拗寮寥夭凹僥踊蓉茸聳涌嵎隅迂虞寓隕耘殞暈冤鴛阮猿萎鍮蹂諭諛紐癒琉溜游柚揄愉宥喩戮淪慄絨戎蔭揖膺誼毅椅擬弛姨餌裡罹痢痍爾翌匿鱗靭蚓燐湮咽吝溢佚淋粒笠孕剩藉蔗疵瓷煮炙仔鵲雀芍綽炸灼嚼勺盞棧簪箴醬薔漿檣杖匠仗齋滓錚豬觝邸躇詛箸狙咀迹謫炙狄嫡餞顫顚銓輾纏篆箭箋癲煎澱氈栓悛廛奠塡剪截霑粘靖碇睛町挺幀靖錠釘酊穽梯悌啼蹄阻遭躁詔藻肇繰糟粗稠眺爪漕槽棗曹嘲凋簇猝踵踪腫慫挫輳躊誅註紬紂廚嗾呪胄做蠢竣樽櫛葺汁肢祉枳摯咫疹嗔迭跌膣桎帙嫉叱朕斟什澄蹉嗟叉鑿窄搾篡饌纂撰擦讖讒站懺塹僭菖艙脹瘡猖漲槍愴廠娼倡寨柵凄脊瘠滌擲闡穿擅喘轍綴凸諂籤僉貼疊牒捷帖諦涕醋貂蕉稍礁硝炒樵梢憔囑忖塚寵塚叢撮鰍鎚錘錐酋芻樞椎墜黜贅萃膵悴脆翠娶惻馳緻癡痔熾幟嗤侈勅鍼砧蟄秤駝陀舵楕惰唾鐸擢綻憚坦呑眈搭蕩宕跆苔笞汰撐攄桶慟筒頹褪腿槌堆妬套慝跛芭琶爬巴婆辦稗牌沛悖唄佩膨澎愎騙鞭貶萍杮陛斃庖逋褒袍蒲脯疱泡圃哺咆匍輻瀑曝飄豹慓剽稟諷披疋逼乏霞遐蝦瑕瘧謔壑罕澣悍轄鹹銜緘涵檻喊函蛤盒肛缸骸駭邂諧楷懈咳偕劾饗嚮墟噓歇衒絢眩頰狹挾俠荊醯彗糊瑚琥狐弧渾笏惚訌虹哄廓鰥驩宦喚闊猾遑煌慌惶恍徨凰賄誨蛔膾繪晦恢徊酵爻嚆哮逅朽嗅吼暈喧喙卉麾諱彙恤洶兇痕欣歆欠洽恰犧詰'
grade_special = '跏訶茄痂珂枷慤稈磵桿柬侃蝎碣曷乫龕鑒橄戡嵌坎胛鱇襁舡羌絳畺强堈鎧盖疥愷喀粳鋸鉅遽踞祛炬据騫蹇楗愆黔鈐瞼劒迲抉鎌鉗箝慊逕耿絅璥烱涇暻擎坰勍倞俓谿誡稽磎棨屆堺誥蠱藁菰苽羔睾沽槁暠攷尻斛鯤琨滾梱崑蚣珙控鍋跨菅罐瓘适恝筐珖炚洸侊紘鮫餃蕎翹嶠耈銶逑絿瞿毬廐坵咎勾麴鞫裙堀芎淃蕨獗饋晷赳竅槻匀鈞筠畇勻菫芹懃劤衿芩檎昑妗伋饑錤錡耭祺祇祁磯碁璂玘夔埼圻桔佶蘿娜喇珞襤湳楠枏嵐柰秊捻拈恬寗瑙櫓菉縷嫩杻鄲袒彖亶獺澾錟覃蕁聃湛坍啖沓戇幢黛玳岱坮韜覩櫂棹嶋纛犢牘焞暾旽墩潼仝逗荳竇枓遯芚嶝蘿喇珞欒襤纜欖攬擥嵐螂瑯琅徠崍粮凉驢蠣藜櫚儷靂轢璉攣洌冽聆翎羚笭怜岺伶澧鹵輅瀘潞櫓菉瀧朧賚瀨鬧蓼廖鏤褸蔞縷瘻婁瑠瀏榴旒侖鯉莉羸璃狸犁浬唎厘藺璘潾霖琳砬碼瑪邈曼巒万茉唜邙輞莽驀陌氓冪麵蓂茗瞑椧芼眸瑁摹姆鶩朦錨竗鵡繆珷楙无懋雯吻刎們沕黴謎湄渼楣梶嵋緡泯愍岷雹璞磐盼瘢泮蚌蒡舫磅滂褙裴盃焙栢佰燔樊幡琺霹蘗檗鱉騈輧棅幷褓珤湺輹蔔茯宓乶琫熢峰趺莩艀缶溥孚鳧賁汾昐菲粃秘毗榧枇斐玭牝浜檳斌騁駟裟莎肆篩砂渣梭柶僿俟伺乍霰蒜汕乷衫芟杉颯鈒牀湘橡廂峠賽穡笙鋤絮筮栖捿墅蓆淅汐饍鐥跣詵蟬蘚癬琁渲敾嬋僊齧褻楔贍剡腥筬珹猩惺宬笹韶銷篠炤瀟溯嘯謖涑飡蓀巽淞釗鬚隧銹邃讐藪蓚茱脩綬綏璲琇燧漱峀岫嗽璹琡潚錞諄詢蕣蓴橓楯栒恂徇鉥嵩崧蝨褶陞蠅豕蓍蒔翅恃屎尸嘶篒寔埴藎莘侁諶芯沁鵝鴉蛾莪峨娥齷鰐鍔鄂渥幄嶽鮟菴岩唵狎昻碍厓掖鸚罌椰蒻穰禳痒煬瀁暘敭凉佯齬馭檍偃蘖孼淹俺嶪円璵歟轝茹艅礖轢縯秊璉烟涓涎沇挻娟堧嚥髥苒琰捻曄煐瀯瀛濚潁渶楹怜嶸塋霙鍈聆羚纓穎瓔獰霓蘂猊汭叡刈倪乂鼇鰲蜈筽獒熬澳晤旿敖塢俉縕瘟瑥兀兀饔癰瓮蛙窪窩豌脘翫碗琬琓浣椀梡娃嵬蟯蓼繞繇瑤燿橈嶢褥縟甬湧榕慂墉埇冗俑雩釪藕芋紆禑盂瑀玗旴稶栯彧勖蕓熉澐橒亐轅爰湲洹沅愿寃嫄垣鉞暐褘蝟蔿葦瑋釉逾萸臾瑜猷濡洧楢杻攸孺侑毓堉贇玧奫聿瀜慇蟻薏艤懿倚彛飴邇貽荑苡肄謚瀷靷藺茵絪璘馹荏稔恁姙卄芿仍茨孜咨斫潺孱岑贓臧牆欌樟暲齎縡渽梓諍箏齟雎這藷菹苧紵疽猪渚樗楮杵姐儲佇鏑迪荻翟吊勣鐫鈿詮筌畑琠塼佺佃癤浙鮎点岾摺玎炡瀞湞渟淀檉柾晸姃霆鋌鉦諪綎薺臍霽醍雕蚤窕璪晁俎鏃鐘淙棕悰倧冑酎蛛綢籌炷澍湊姝侏粥雋逡畯焌寯儁茁楫繒甑烝拯趾贄蜘芷祗砥漬沚軫賑袗蔯臻縝縉瞋畛璡瑨溱殄榛桭晉搢唇蛭瓆侄鏶緝潗箚磋嵯侘齪纘粲簒竄澯紮釵綵砦寀蹠慽剔倜韆阡舛玔仟輟詹簽甛沾輒睫堞鯖菁剃醮酢苕艸椒剿矗邨蔥摠憁悤騶雛諏萩皺湫蹙筑竺瑃朮鷲驟嘴厠仄輜蚩緇穉痴淄梔飭柒琛馱朶拖咤琸柝晫坼啄倬嘆榻帑邰撑兎偸闖杷擺鈑瓣坂捌叭覇狽浿烹翩枰嬖吠苞匏佈驃飇瓢彪俵陂馝苾珌鰕昰廈厦閒瀚啣闔閤哈桁杭嫦姮伉蟹瀣孩垓荇倖餉珦櫶奕舷睍玹泫晛俔頁孑鋏莢脇浹夾鎣逈珩熒灐滎泂鞋蹊蕙暳顥頀蝴蒿葫芦縞瓠灝濩滸淏岵壺琿烘汞譁畵攫碻紈渙晥奐豁隍蝗簧篁璜潢湟榥晄愰幌茴獪澮匯鐄宖驍肴淆涍梟斅珝煦帿塤勛燻焄薨萱煊暄煇暉虧畦鷸譎炘昕訖紇屹吃翕凞熺曦晞戱憘囍凞僖葭珈檟斝哿桷卻蕑瞯衎玕榦秸减酣矙歛欿橿杠湝嘅喈玠槩秔鏗賡硜臄虡琚椐袪蘧莒籧筥秬褰朅跲愒鵙繳綌鴃鬲豣睊獧岍蠲繾畎狷觼袺闋蒹歉鶊睘牼冂黥駉褧罄熲焭煢檠惸冏笄雞烓稾鼛翶罛楛酤觚羖罟瞽盬櫜槀栲杲刳牿轂觳鯀棞髡錕緄邛悾蜾薖裹夸鞹霍躩瘝痯鸛錧綰祼盥丱聒栝佸迋誑纊桄蕢瑰虢鞃觥鷮荍茭曒敽儌蹻磽姣嘐佼雊觩艽笱韭遘覯裘糗窶疚璆漚搆捄扣彀屨嫗媾姤劬俅匊詘鬈綣睠棬簣垝匭餽跪簋氿匱宄騤頄戣頍闚糺睽樛刲麕箘郤襋殛亟漌墐岌亙軝覊蘷芑頎跂羇綦歧棊曁暣旂掎忮屺墍僛姞戁赧陧軜曩鼐迺甯佞砮怓猱峱孥呶穠餒耨鈕狃忸你柅怩昵爹襢煅癉漙慱闥怛髧驔餤萏菼耼窞惔黮螗鐺鏜儻倘譈祋憝懟鞉謟荼翿綯瘏咷鼗闍稌洮檮擣慆忉叨匵黷櫝罿烔蝀彤僮侗斁螣縢滕蠃臝雒瓓闌捋稂勑倈騋藘蠡膂厲酈櫟孌栵蘞蛉苓昤姈鱧纑簵壚彔隴耒罍敹繚潦摟駵虆藟罶懰纍穋僇懍廩詈纚縭梩莅离涖俐鄰粼苙禡瘼鏋墁秣蘉韎霾鋂脢痗浼勱苺沬霢貉薁糹糸湎幭篾麰髳髦蟊耄眊旄霂楘饛矇濛幪茆貓藐眇膴廡儛纆璊炆捫郿穈麋糜瀰敉弭亹痻潣敃慜黽暋忞鉑襮鎛亳鞶胖軷茇浡雱逄魴幫厖桮墦袢蘩翻杋甓釆籩荓怲迸缾黼鴇鍑葍楅濮扑芃唪菶丰紑痡鮒鈇裒蜉芣罦祔桴掊拊俘鼖饙豶苯幩蕡濆棼枌紼笰巿咈黻茀艴紱駓鞞篚秠畀朏岯奰伾騑霏閟轡貔芾腓羆紕痹淠棐悱庳埤圮剕俾仳蠙璸鬢邠豳蘋繽擯儐蹝蓰葸耜簑涘戺鯊笥汜榭傞鑠潸歃鱨顙殤塽眚鱮諝藇癙紓澨湑婿噬裼螫鼫鉐舃腊珗毨墠僎熯愃墡絏挈紲暬偰憸韘娍騂瑆洒帨蠨玿柖慅愫霄蛸艘翛繅愬埽餗觫藚蔌樕飱飧蟀竦瑣魗繻穟檖豎瞍睢睟濉殳廋售叟橚俶郇犉漘鶉肫璱隰熠鳲釃諟緦枲塒啻兕偲栻甡璶駪贐矧哂蟋諗葚迓咢鴈犴歹戛頞遏訐揠黯鞅盎泱卬餲藹僾頟阨戹嚶瀹籥禴饟鍚昜颺瀼漾饇飫敔圉鰋唁臲孽臬渰揜閹鸒畬洳旟鷊鶂罭緎棫晹埸閾淢懌嶧醼蜎掾悁兗噎艷燄饜檿冉饁爗攖郢贏縈嬴咏輗蓺羿瘞橤堄勩麑鷖蚋蕊翳睨珸杇奡嗸隩汙忤鋈韞醞昷慍媼杌扤卼灉顒雝廱吪菀婠盌垸騧鷕葽蕘殀徼徭喓鄘踴宂訧訏楀懮噳麌麀踽耰耦盱堣吁俁稢勗燠篔沄黿騵圜軏刖藯韡闈煒喟醹輶褎羑秞濰滺槱楰曘卣龥黝鮪蝤莠緌籲窬牖揉帷囿呦阭狁鴥驈繘汩訔溵檼憖嚚浥挹薿扆饐猗嶷劓頤詒苢樲桋杝异刵迤訑洟彝弋駰陻闉軔訒牣禋夤仞泆袵衽陾鼒訿胏秭鎡赭貲訾茲胾耔粢泚柘孶柞僝粻斨鏘萇牂漳戕奘賫纔灾羜筯砠疷苴羝罝氐杼踖趯籊逖覿糴闐瘨牷瀍鱣飦顓靦邅荃腆翦畋瑱旃戩巓晣晢坫覘簟玷墊阱赬裎涏靚鋥酲珵棖梃桯鵜隮蠐泲懠嚌穧隄躋稊禔瑅娣鰷鞗阼螬蓧罩皂旐慥恌鼂蜩蔦竈皁殂懆徂佻鬷豵尰蹤螽瑽樅椶脞馵邾躕譸燽妵咮霔遒輈裯幬侜鬻鱒隼蹲埻噂崒騭濈璔鋕輊蚳踟篪坻螓紾禛鬒蓁銍耋礩瓞挃蒺絰垤縶戢佌瑳佽斮斲湌爨巑扎譖毚憯韔鶬鬯蹌窗瑲搶悵蠆瘵瘥簀萋蹢蹐慼跖惕坧遄梴幝倩俴驖歠掇惙啜餂襜忝髢遆蝃禘疐杕揥掣嚔棣彘譙誚悄勦蠋躅潨冢凗摧嘬鄹萑緅棸麤鶖鵻魋騅縐瘳甃顣踧蓫柷蹜妯賰杶怵珫忡瘁揣惴毳昃廁觶懫懥庤鴟褫菑絺寘哆綅寑駸忱夬噲紽嶞它鼉鮀沱佗椓蘀橐疃嘽僤驒殫梲醓嗿漯蝪簜盪駾迨畽啍瓲噸噋恫蓷隤渝忒豝嶓簸皤昄茷粺旆孛伻祊諞褊徧苹敝麃襃餔炰炮飆瀌滮儦鑣殍摽嘌豐灃葑辟詖飶鉍怭駜鞸觱佖偪騢菏芐嘏呀翯扞哻暵僩舝劼鬫諴菡盍柙嗑頏陔醢覈悻栩巘玁獫衋虩焃侐焱洫怰鞙莧駽昡嬛儇絜冾恊譓憓盻徯嘒傒薅皥嘑皜怙惛洚鬨鉷擭雘矍雈逭芄鐶鍰豢睆懽濶堭媓喤薈頮洄鴞嘵効虓熇殽囂傚鍭餱酗詡鑂纁貆咺諼諠虺虫翬觿攜咻遹訩釁忻齕迄汔仡潝饎橲餼豨爔嘻咥襭'

def get_meaning(hanja):
    url = f'https://hanja.dict.naver.com/hanja?q={hanja}&cp_code=0&sound_id=0'
    response = requests.get(url)
    if response.status_code != 200:
        pritn(f'Failed request: {r.status_code}')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find('div', class_='kinds_list')
    if res is None:
        return None
    return '\n'.join(li.get_text().strip() for li in res.ul.findAll("li", recursive=False))


def get_sample():
    syms = \
    """
    校
    敎
    九
    國
    軍
    釒
    金
    南
    女
    年
    大
    東
    六
    萬
    母
    木
    """

    for sym in syms.split('\n'):
        sym = sym.strip()
        if len(sym) == 0:
            continue
        print(sym.strip())
        print(get_meaning(sym.strip()))


def write_article(cjk_sym, contents, root_dir):
    # Creates article files: 000001/000001.txt, ..., 00900/00900.txt, ...
   # root_dir = 'naver_hanja'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    unicode_num = ord(cjk_sym)
    dir_num = (unicode_num // 100) * 100 if unicode_num >= 100 else 1
    dir_name = f'{dir_num:06}'
    #print(dir_name)
    if not os.path.exists(os.path.join(root_dir, dir_name)):
        os.mkdir(os.path.join(root_dir, dir_name))
    with open(os.path.join(root_dir, dir_name, f'{unicode_num:06}.txt'), mode='w', encoding='utf8') as f:
        f.write(contents)


def get_by_order():
    root = 'naver_hanja'
    for index, hanja in enumerate(grade_special[1640:]):
        contents = get_meaning(hanja)
        if contents is None:
            print(f'{hanja}: empty contents')
        write_article(hanja, contents, root)
        print(index, hanja)
        time.sleep(0.1)


#print(get_meaning('霸'))
get_by_order()