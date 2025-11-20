from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

# -----------------------------
# SIMPLE DICTIONARY QA ENGINE
# -----------------------------
from typing import Dict, Any

QA_DATASET: Dict[str, Dict[str, Any]] = {
    # ----------------------------------------------------------------------
    # १. मूलभूत माहिती आणि नियोजन (General Metrics & Planning)
    # ----------------------------------------------------------------------
    "what_is_cropeye": {
        "keywords": [ "cropeye", "cropeye काय आहे", "cropeye क्या है", "what is cropeye"],
        "mr": "CropEye.ai हे प्रगत प्रेसिजन शेतीचे (Precision Farming) साधन  आहे. हे AI आणि उपग्रह (Satellite) तंत्रज्ञान  वापरून तुमच्या शेतातील पिकांचे आरोग्य, उत्पादन अंदाज आणि पाणी-खत व्यवस्थापनासाठी  अचूक आणि तत्काळ मार्गदर्शन  करते. याचे मुख्य उद्दिष्ट तुम्हाला  डेटा-आधारित निर्णय  घेण्यास मदत करणे आहे.",
        "hi": "CropEye.ai एक  एडवांस्ड प्रिसीजन फार्मिंग समाधान  है जो AI, सैटेलाइट इमेजरी और डेटा विश्लेषण  का उपयोग करके आपके खेत में फसल के स्वास्थ्य, उपज अनुमान, और संसाधन प्रबंधन (पानी, खाद) के लिए  वास्तविक समय की, कार्रवाई योग्य जानकारी  प्रदान करता है।",
        "en": "CropEye.ai is a  comprehensive precision farming solution  that uses  AI, satellite imagery, and data analysis  to provide real-time, actionable insights for crop health, yield optimization, and resource management (water, fertilizer) on your farm. Its main goal is to help you make  data-driven decisions ."
    },
    "cropeye": {
        "keywords": [ "cropeye", "crop", "cropeye क्या है", "what is cropeye"],
        "mr": "CropEye.ai हे प्रगत प्रेसिजन शेतीचे (Precision Farming) साधन  आहे. हे AI आणि उपग्रह (Satellite) तंत्रज्ञान  वापरून तुमच्या शेतातील पिकांचे आरोग्य, उत्पादन अंदाज आणि पाणी-खत व्यवस्थापनासाठी  अचूक आणि तत्काळ मार्गदर्शन  करते. याचे मुख्य उद्दिष्ट तुम्हाला  डेटा-आधारित निर्णय  घेण्यास मदत करणे आहे.",
        "hi": "CropEye.ai एक  एडवांस्ड प्रिसीजन फार्मिंग समाधान  है जो AI, सैटेलाइट इमेजरी और डेटा विश्लेषण  का उपयोग करके आपके खेत में फसल के स्वास्थ्य, उपज अनुमान, और संसाधन प्रबंधन (पानी, खाद) के लिए  वास्तविक समय की, कार्रवाई योग्य जानकारी  प्रदान करता है।",
        "en": "CropEye.ai is a  comprehensive precision farming solution  that uses  AI, satellite imagery, and data analysis  to provide real-time, actionable insights for crop health, yield optimization, and resource management (water, fertilizer) on your farm. Its main goal is to help you make  data-driven decisions ."
    },
    "field_area_measurement": {
        "keywords": ["फील्ड एरिया", "field area", "खेत का क्षेत्रफल", "क्षेत्रफल कैसे मापा"],
        "mr": "CropEye.ai तुमच्या शेताच्या GPS आणि उपग्रह प्रतिमा (Satellite Imagery) डेटा वापरून नकाशावर सीमांकन (Geo-fencing) करून अचूक मापन करते.",
        "hi": "CropEye.ai आपके खेत के GPS और उपग्रह छवियों (Satellite Imagery) का उपयोग करके मानचित्र पर जियो-फेंसिंग करके सटीक मापन करता है।",
        "en": "CropEye.ai performs accurate measurement by using GPS and satellite imagery data to define the boundaries (Geo-fencing) of your farm on the map."
    },
    "field":{
        "keywords": ["फील्ड", "field", "खेत का क्षेत्रफल", "क्षेत्रफल कैसे मापा"],
        "mr": "CropEye.ai तुमच्या शेताच्या GPS आणि उपग्रह प्रतिमा (Satellite Imagery) डेटा वापरून नकाशावर सीमांकन (Geo-fencing) करून अचूक मापन करते.",
        "hi": "CropEye.ai आपके खेत के GPS और उपग्रह छवियों (Satellite Imagery) का उपयोग करके मानचित्र पर जियो-फेंसिंग करके सटीक मापन करता है।",
        "en": "CropEye.ai performs accurate measurement by using GPS and satellite imagery data to define the boundaries (Geo-fencing) of your farm on the map."
    },
    "crop_status_change": {
        "keywords": ["क्रॉप स्टेटस", "पीक स्थिती", "crop status", "फसल की स्थिति"],
        "mr": "हा बदल पिकाच्या वाढीच्या टप्प्यावर आधारित असतो. हे AI मॉडेल पिकाच्या वाढीचे विश्लेषण करून आणि तुम्ही पेरणीची तारीख नोंदवल्यावर निश्चित होते.",
        "hi": "यह परिवर्तन फसल के विकास चरण पर आधारित होता है। यह AI मॉडल फसल की वृद्धि का विश्लेषण करके और आपके बुवाई की तारीख दर्ज करने पर निर्धारित होता है।",
        "en": "This change is based on the crop's growth stage. It is determined by the AI model analyzing crop growth and the planting date you entered."
    },
    "days_to_harvest_negative": {
        "keywords": ["डेज टू हार्वेस्ट नकारात्मक", "harvest negative", "नकारात्मक संख्या", "कटाई के दिन माइनस"],
        "mr": "नकारात्मक संख्या याचा अर्थ  नियोजित कापणीची वेळ निघून गेली आहे  आणि पीक उशिरा काढले जात आहे किंवा शेड्यूलमध्ये बदल करणे आवश्यक आहे.",
        "hi": "नकारात्मक संख्या का अर्थ है कि  योजनाबद्ध कटाई का समय निकल चुका है  और फसल देर से काटी जा रही है या आपको शेड्यूल बदलना होगा।",
        "en": "A negative number means the  planned harvest time is overdue , and the crop is being harvested late, or the schedule needs adjustment."
    },
    "sugar_content_harvest": {
        "keywords": ["साखर कंटेंट कापणी", "sugar content harvest", "शुगर कंटेंट", "रिकव्हरी मिळेल"],
        "mr": "ऊस पिकासाठी, साखरेचा  'सरासरी ब्रिक्स' (Avg Brix)  जेव्हा विशिष्ट पातळीपेक्षा जास्त (उदा. १९-२०) होतो, तेव्हा कापणीसाठी तोडगा काढणे फायदेशीर ठरते.",
        "hi": "गन्ने की फसल के लिए, जब चीनी का  'औसत ब्रिक्स' (Avg Brix)  एक निश्चित स्तर से ऊपर (जैसे १९-२०) हो जाता है, तब कटाई का निर्णय लेना फायदेमंद होता है।",
        "en": "For sugarcane, it is profitable to decide on harvesting when the  'Avg Brix'  level goes above a specific threshold (e.g., 19-20)."
    },
    "sugar_content_max_min": {
        "keywords": ["मॅक्स मिन शुगर कंटेंट", "max min sugar", "कमाल किमान साखर"],
        "mr": "ही मूल्ये शेताच्या विविध विभागातून (उदा. नमुना घेऊन) घेतलेल्या मापनांवर आधारित असतात, जेणेकरून शेतातील  साखरेच्या गुणवत्तेतील तफावत  कळेल.",
        "hi": "ये मान खेत के विभिन्न हिस्सों (जैसे नमूना लेकर) से लिए गए मापों पर आधारित होते हैं, ताकि खेत में  चीनी की गुणवत्ता में अंतर  पता चले।",
        "en": "These values are based on measurements taken from various sections of the field (e.g., by sampling) to show  variation in sugar quality  across the farm."
    },
    "irrigation_schedule_change": {
        "keywords": ["सिंचन वेळापत्रक आपोआप बदलते", "irrigation schedule auto change", "सिंचाई का समय"],
        "mr": "होय, CropEye.ai चे 'इरिगेशन शेड्यूल' (Irrigation Schedule) पिकाच्या टप्प्यांमध्ये पाण्याच्या गरजेनुसार  आपोआप बदलले जाते .",
        "hi": "हाँ, CropEye.ai का 'सिंचाई शेड्यूल' (Irrigation Schedule) फसल के चरणों में पानी की आवश्यकता के अनुसार  स्वचालित रूप से बदल जाता है ।",
        "en": "Yes, CropEye.ai's 'Irrigation Schedule' is  automatically adjusted  according to the water needs during the crop stages."
    },
    "field_area_difference": {
        "keywords": ["एरिया वेगळा का आहे", "field area difference", "क्षेत्रफल अलग क्यों है"],
        "mr": "तुमचा नोंदणीकृत एरिया तुमच्या GPS नोंदीवर आधारित आहे. शेजारच्या शेताचा एरिया त्यांच्या नोंदी आणि उपग्रह नकाशावर काढलेल्या त्यांच्या हद्दीनुसार निश्चित होतो.",
        "hi": "आपका पंजीकृत क्षेत्रफल आपके GPS रिकॉर्ड पर आधारित है। पड़ोसी खेत का क्षेत्रफल उनके रिकॉर्ड और उपग्रह मानचित्र पर खींची गई उनकी सीमाओं के अनुसार निर्धारित होता है।",
        "en": "Your registered area is based on your GPS records. The neighbor's area is determined by their records and the boundaries drawn on the satellite map."
    },
    "harvest_days_yield_impact": {
        "keywords": ["हार्वेस्ट डेज चुकल्यास", "harvest days missed impact", "उत्पन्नावर परिणाम"],
        "mr": "ऊस जास्त पिकल्यास (Over-ripening), साखरेचे प्रमाण कमी होऊ शकते आणि पिकाचा  'रिकव्हरी रेट' घटू शकतो , ज्यामुळे आर्थिक नुकसान होते.",
        "hi": "गन्ना ज्यादा पकने पर (Over-ripening), चीनी की मात्रा कम हो सकती है और फसल का  'रिकवरी रेट' घट सकता है , जिससे आर्थिक नुकसान होता है।",
        "en": "If sugarcane is over-ripened, the sugar content may decrease, and the crop's  'Recovery Rate' can drop , leading to financial loss."
    },
    "crop_status_suitability": {
        "keywords": ["क्रॉप स्टेटस योग्य आहे", "crop status suitability", "स्थिति सही है या नहीं"],
        "mr": "तुमच्या पीक स्थितीची तुलना CropEye.ai मधील त्याच हंगामातील  (Regional Best Practices) इष्टतम वाढीच्या टप्प्यांशी  केली जाते.",
        "hi": "आपकी फसल की स्थिति की तुलना CropEye.ai में उसी सीजन के  (Regional Best Practices) इष्टतम विकास चरणों  से की जाती है।",
        "en": "Your crop status is compared with the  optimal growth stages (Regional Best Practices)  for the same season within CropEye.ai."
    },
    "crop_status_manual_change": {
        "keywords": ["क्रॉप स्टेटस मी बदलू शकतो", "crop status manual change", "स्थिति खुद बदल सकते हैं"],
        "mr": "बहुतेक वेळा CropEye.ai ते आपोआप ठरवते, परंतु तुम्ही तुमच्या व्यवस्थापकाशी संपर्क साधून किंवा ॲपमध्ये आवश्यक इनपुट देऊन  बदल सुचवू शकता .",
        "hi": "अधिकांश समय CropEye.ai इसे स्वचालित रूप से निर्धारित करता है, लेकिन आप अपने प्रबंधक से संपर्क करके या ऐप में आवश्यक इनपुट देकर  बदलाव सुझा सकते हैं ।",
        "en": "Most of the time CropEye.ai determines it automatically, but you can  suggest changes  by contacting your manager or providing necessary input in the app."
    },
    # ----------------------------------------------------------------------
    # २. फील्ड इंडायसेस (Field Indices) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "growth_index_low_reason": {
        "keywords": ["ग्रोथ इंडेक्स कमी का", "growth index low reason", "ग्रोथ इंडेक्स कम क्यों"],
        "mr": "'ग्रोथ इंडेक्स' कमी होण्याची मुख्य कारणे म्हणजे  पाण्याची कमतरता , पोषक तत्वांची (उदा. नायट्रोजन) कमतरता किंवा पिकावर आलेला  ताण (Stress) .",
        "hi": "'ग्रोथ इंडेक्स' कम होने के मुख्य कारण  पानी की कमी , पोषक तत्वों (जैसे नाइट्रोजन) की कमी या फसल पर आया हुआ  तनाव (Stress)  हैं।",
        "en": "The main reasons for a low 'Growth Index' are  water deficit , lack of nutrients (e.g., Nitrogen), or  stress  on the crop."
    },
    "growth_index_optimal_level": {
        "keywords": ["ग्रोथ इंडेक्स कोणत्या पातळीवर", "growth index optimal level", "ग्रोथ इंडेक्स स्तर"],
        "mr": "पिकाच्या प्रकारानुसार आणि टप्प्यानुसार ही पातळी बदलते, परंतु शक्यतो हा निर्देशांक  उच्च पातळीवर (उदा. ०.७५ च्या वर)  आणि स्थिर राखणे फायदेशीर असते.",
        "hi": "फसल के प्रकार और चरण के अनुसार यह स्तर बदलता है, लेकिन इसे  उच्च स्तर (जैसे ०.७५ से ऊपर)  और स्थिर बनाए रखना फायदेमंद होता है।",
        "en": "This level varies by crop type and stage, but it is beneficial to maintain the index at a  high level (e.g., above 0.75)  and stable."
    },
    "growth_index_low_fertilizer": {
        "keywords": ["ग्रोथ इंडेक्स सुधारणा खत", "growth index fertilizer", "ग्रोथ इंडेक्स खाद", "युरिया"],
        "mr": "ग्रोथ इंडेक्स थेट  नायट्रोजनच्या कमतरतेशी  संबंधित असतो. त्यामुळे नायट्रोजनयुक्त खत (उदा. युरिया) त्वरित देण्याची शिफारस केली जाते.",
        "hi": "ग्रोथ इंडेक्स सीधे  नाइट्रोजन की कमी  से संबंधित होता है। इसलिए, नाइट्रोजन युक्त खाद (जैसे यूरिया) तुरंत देने की सिफारिश की जाती है।",
        "en": "The Growth Index is directly linked to  Nitrogen deficiency . Therefore, immediate application of Nitrogen-rich fertilizer (e.g., Urea) is recommended."
    },
    "growth_index_low_multi_reason": {
        "keywords": ["खताच्या कमतरतेमुळे की पाणी", "growth index multi reason", "ग्रोथ इंडेक्स कारण"],
        "mr": "हे  तिन्ही कारणामुळे  होऊ शकते. अचूक कारण ओळखण्यासाठी ग्रोथ इंडेक्सची तुलना 'वॉटर इंडेक्स' (पाणी) आणि 'स्ट्रेस इंडेक्स' (रोग/ताण) सोबत केली पाहिजे.",
        "hi": "यह  तीनों कारणों  से हो सकता है। सटीक कारण जानने के लिए ग्रोथ इंडेक्स की तुलना 'वॉटर इंडेक्स' (पानी) और 'स्ट्रेस इंडेक्स' (रोग/तनाव) के साथ की जानी चाहिए।",
        "en": "It can be due to  all three reasons . To identify the exact cause, the Growth Index must be compared with the 'Water Index' (water) and 'Stress Index' (disease/stress)."
    },
    "growth_index_biomass_relation": {
        "keywords": ["ग्रोथ इंडेक्स बायोमास संबंध", "growth index biomass relation", "बायोमास संबंध"],
        "mr": "'ग्रोथ इंडेक्स' (NDVI) हे पिकाच्या हिरवेपणाचे आणि घनतेचे मापन आहे. उच्च 'ग्रोथ इंडेक्स' म्हणजे  जास्त 'बायोमास'  आणि उच्च उत्पादन संभाव्यता.",
        "hi": "'ग्रोथ इंडेक्स' (NDVI) फसल के हरेपन और घनत्व का मापन है। उच्च 'ग्रोथ इंडेक्स' का अर्थ है  अधिक 'बायोमास'  और उच्च उत्पादन क्षमता।",
        "en": "The 'Growth Index' (NDVI) is a measure of crop greenness and density. A higher 'Growth Index' means  more 'Biomass'  and higher yield potential."
    },
    "stress_index_high_first_step": {
        "keywords": ["स्ट्रेस इंडेक्स वाढल्यास उपाययोजना", "stress index high first step", "स्ट्रेस इंडेक्स उपाय"],
        "mr": "'स्ट्रेस इंडेक्स' वाढल्यास प्रथम  मातीतील ओलावा तपासावा . पाण्याची कमतरता असल्यास  त्वरित सिंचन  सुरू करावे.",
        "hi": "'स्ट्रेस इंडेक्स' बढ़ने पर, सबसे पहले  मिट्टी की नमी जांचें । पानी की कमी होने पर  तुरंत सिंचाई  शुरू करें।",
        "en": "If the 'Stress Index' is high, first  check the soil moisture . If there is a water deficit,  start irrigation immediately ."
    },
    "stress_index_danger_zone": {
        "keywords": ["स्ट्रेस इंडेक्स धोक्याची घंटा", "stress index danger zone", "खतरे का स्तर"],
        "mr": "पिकाच्या प्रकारानुसार 'धोक्याची पातळी' बदलते, परंतु  उच्च पातळीवर (उदा. ०.५० च्या वर)  आणि सतत वाढत असलेला निर्देशांक त्वरित उपचाराची गरज दर्शवतो.",
        "hi": "फसल के प्रकार के अनुसार 'खतरे का स्तर' बदलता है, लेकिन  उच्च स्तर पर (जैसे ०.५० से ऊपर)  और लगातार बढ़ता हुआ इंडेक्स तत्काल उपचार की आवश्यकता दर्शाता है।",
        "en": "The 'danger level' varies by crop type, but an index at a  high level (e.g., above 0.50)  and continuously rising indicates an immediate need for treatment."
    },
    "stress_index_yield_loss": {
        "keywords": ["उच्च स्ट्रेस इंडेक्समुळे नुकसान", "stress index yield loss", "उत्पादनात घट"],
        "mr": "उच्च ताणामुळे प्रकाशसंश्लेषण (Photosynthesis) थांबते, पिकाची वाढ खुंटते आणि थेट  उत्पादनात (Yield) मोठी घट  होते.",
        "hi": "उच्च तनाव के कारण प्रकाश संश्लेषण (Photosynthesis) रुक जाता है, फसल की वृद्धि रुक जाती है और सीधे  उत्पादन (Yield) में भारी कमी  आती है।",
        "en": "High stress halts photosynthesis, stunts crop growth, and directly leads to a  significant decrease in yield ."
    },
    "stress_index_water_vs_heat": {
        "keywords": ["पाण्याची कमतरता की उष्णतेचा ताण", "water vs heat stress", "पानी की कमी या गर्मी का तनाव"],
        "mr": "पाण्याची कमतरता असल्यास 'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' दोन्ही कमी झालेले दिसतील, तर फक्त उष्णतेचा ताण असल्यास फक्त  पानांचे तापमान वाढलेले  दिसेल (थर्मल स्ट्रेस).",
        "hi": "पानी की कमी होने पर 'वॉटर इंडेक्स' और 'मॉइश्चर इंडेक्स' दोनों कम दिखेंगे, जबकि केवल गर्मी का तनाव होने पर केवल  पत्तियों का तापमान बढ़ा हुआ  दिखेगा (थर्मल स्ट्रेस)।",
        "en": "Water deficit will show low 'Water Index' and 'Moisture Index', whereas only heat stress will show  increased leaf temperature  (Thermal Stress)."
    },
    "stress_index_disease_detection": {
        "keywords": ["स्ट्रेस इंडेक्स रोग ओळखू शकतो", "stress index disease detection", "रोग पहचान"],
        "mr": "'स्ट्रेस इंडेक्स' पानांच्या रंग आणि संरचनेतील बदलांवरून  रोगांमुळे आलेला ताण  (उदा. बुरशीजन्य रोग) ओळखू शकतो, परंतु विशिष्ट रोगाचे नाव देण्यासाठी त्याला अधिक विश्लेषणाची गरज असते.",
        "hi": "'स्ट्रेस इंडेक्स' पत्तियों के रंग और संरचना में बदलाव से  रोगों के कारण हुए तनाव  (जैसे फंगल रोग) को पहचान सकता है, लेकिन विशिष्ट रोग का नाम बताने के लिए उसे अधिक विश्लेषण की आवश्यकता होती है।",
        "en": "The 'Stress Index' can identify  stress caused by diseases  (e.g., fungal diseases) based on changes in leaf color and structure, but requires more analysis to name the specific disease."
    },
    "water_vs_moisture_index": {
        "keywords": ["वॉटर इंडेक्स मॉईश्चर इंडेक्स फरक", "water moisture index difference", "पानी और नमी सूचकांक"],
        "mr": " 'वॉटर इंडेक्स'  पिकाच्या  पानांमधील पाण्याची मात्रा  दर्शवतो, तर  'मॉईश्चर इंडेक्स'   मातीतील ओलाव्याचे प्रमाण  दर्शवतो.",
        "hi": " 'वॉटर इंडेक्स'  फसल की  पत्तियों में पानी की मात्रा  दर्शाता है, जबकि  'मॉइश्चर इंडेक्स'   मिट्टी की नमी की मात्रा  दर्शाता है।",
        "en": "The  'Water Index'  shows the  amount of water in the crop leaves , while the  'Moisture Index'  shows the  amount of moisture in the soil ."
    },
    "moisture_index_irrigation_level": {
        "keywords": ["मॉईश्चर इंडेक्स सिंचन पातळी", "moisture index irrigation level", "नमी सूचकांक सिंचाई"],
        "mr": "जेव्हा 'मॉईश्चर इंडेक्स'  ५०% च्या खाली  जातो, तेव्हा  त्वरित सिंचनाची  शिफारस केली जाते.",
        "hi": "जब 'मॉइश्चर इंडेक्स'  ५०% से नीचे  चला जाता है, तब  तुरंत सिंचाई  करने की सिफारिश की जाती है।",
        "en": "When the 'Moisture Index' drops  below 50% ,  immediate irrigation  is recommended."
    },
    "moisture_index_soil_type": {
        "keywords": ["मातीचा प्रकार मॉईश्चर इंडेक्सवर परिणाम", "soil type moisture index impact", "मिट्टी का प्रकार"],
        "mr": "रेताड माती लवकर पाणी गमावते, तर काळी माती पाणी जास्त काळ टिकवून ठेवते. त्यामुळे  मातीच्या प्रकारानुसार  इंडेक्सची 'धोक्याची पातळी' निश्चित करावी लागते.",
        "hi": "रेतीली मिट्टी जल्दी पानी खो देती है, जबकि काली मिट्टी पानी को लंबे समय तक बनाए रखती है। इसलिए  मिट्टी के प्रकार के अनुसार  इंडेक्स का 'खतरे का स्तर' तय करना पड़ता है।",
        "en": "Sandy soil loses water quickly, while black soil retains water longer. Therefore, the index's 'danger level' must be set  according to the soil type ."
    },
    "water_index_rain_change": {
        "keywords": ["जोरदार पाऊस वॉटर इंडेक्स बदल", "water index rain change", "बारिश के बाद इंडेक्स"],
        "mr": "'वॉटर इंडेक्स' (पानांमधील पाणी) पाऊस थांबल्यानंतर  काही तासांत लगेच सुधारू लागतो , कारण पिके त्वरित पाणी शोषण्यास सुरुवात करतात.",
        "hi": "वॉटर इंडेक्स' (पत्तियों में पानी) बारिश रुकने के बाद  कुछ ही घंटों में तुरंत सुधरने लगता है , क्योंकि फसलें तुरंत पानी सोखना शुरू कर देती हैं।",
        "en": "The 'Water Index' (water in leaves) starts to  improve immediately within a few hours  after the rain stops, as crops start absorbing water quickly."
    },
    "water_index_no_improvement": {
        "keywords": ["सिंचन केल्यावरही वॉटर इंडेक्स सुधारत नाही", "water index no improvement", "सिंचाई के बाद भी"],
        "mr": "याचा अर्थ मुळांना पाणी शोषण्यात अडचण येत आहे. हे कदाचित  माती घट्ट झाल्यामुळे (Compaction)  किंवा मुळांना रोग झाल्यामुळे असू शकते.",
        "hi": "इसका मतलब है कि जड़ों को पानी सोखने में दिक्कत आ रही है। यह शायद  मिट्टी के सख्त होने (Compaction)  या जड़ों में रोग होने के कारण हो सकता है।",
        "en": "This means the roots are having trouble absorbing water. This may be due to  soil compaction  or root diseases."
    },
    # ----------------------------------------------------------------------
    # ३. माती, आरोग्य आणि बायोमास (Soil, Health & Biomass) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "organic_carbon_optimal": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी किती", "organic carbon optimal level", "सेंद्रिय कर्ब", "organic carbon density"],
        "mr": "साधारणपणे, सेंद्रिय कर्बाचे प्रमाण  ०.५% पेक्षा जास्त  (म्हणजेच gm/cm³ मध्ये जास्त) असल्यास मातीची गुणवत्ता चांगली मानली जाते.",
        "hi": "सामान्यतः, यदि कार्बनिक कार्बन की मात्रा  ०.५% से अधिक  (यानी gm/cm³ में अधिक) है तो मिट्टी की गुणवत्ता अच्छी मानी जाती है।",
        "en": "Generally, soil quality is considered good if the organic carbon content is  greater than 0.5%  (i.e., higher in gm/cm³)."
    },
    "organic_carbon_improve": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी सुधारण्यासाठी खत", "improve organic carbon", "सेंद्रिय खत"],
        "mr": " शेणखत, कंपोस्ट खत, गांडूळ खत  किंवा हिरवळीची खते (Green Manure) वापरून 'ऑरगॅनिक कार्बन डेन्सिटी' सुधारता येते.",
        "hi": " गोबर की खाद, कंपोस्ट खाद, केंचुआ खाद  या हरी खाद (Green Manure) का उपयोग करके 'कार्बनिक कार्बन घनत्व' में सुधार किया जा सकता है।",
        "en": " Cow dung manure, compost, vermicompost,  or green manures can be used to improve 'Organic Carbon Density'."
    },
    "soil_ph_sugarcane_optimal": {
        "keywords": ["pH लेव्हल ऊस पिकासाठी योग्य आहे", "soil ph level sugarcane", "pH 7.30"],
        "mr": " ७.३० pH  ऊस पिकासाठी स्वीकार्य आहे (ऊस ६.० ते ८.५ pH मध्ये वाढतो). pH जास्त असल्यास  गंधक (Sulphur)  वापरावा आणि कमी असल्यास  चुना (Lime)  वापरावा.",
        "hi": " ७.३० pH  गन्ने की फसल के लिए स्वीकार्य है (गन्ना ६.० से ८.५ pH में बढ़ता है)। pH अधिक होने पर  सल्फर (Sulphur)  का उपयोग करें और कम होने पर  चूना (Lime)  का उपयोग करें।",
        "en": " 7.30 pH  is acceptable for sugarcane (sugarcane grows in 6.0 to 8.5 pH). Use  Sulphur  if the pH is high and  Lime  if it is low."
    },
    "biomass_yield_projection_relation": {
        "keywords": ["बायोमास उत्पादन अंदाज संबंध", "biomass yield projection relation", "कुल बायोमास"],
        "mr": "'एकूण बायोमास' हे पिकाच्या वाढीचे वर्तमान वजन आहे, जे 'उत्पादन अंदाजा'साठी आधारभूत आहे.  जास्त बायोमास म्हणजे जास्त उत्पादन  मिळण्याची शक्यता.",
        "hi": "'कुल बायोमास' फसल की वृद्धि का वर्तमान वजन है, जो 'उत्पादन अनुमान' के लिए आधार है।  अधिक बायोमास का अर्थ है अधिक उत्पादन  मिलने की संभावना।",
        "en": "Total Biomass is the current weight of crop growth, which is the basis for the 'Yield Projection'.  More biomass means a higher probability of higher yield ."
    },
    "biomass_distribution_measurement": {
        "keywords": ["बायोमासचे वितरण", "biomass distribution measurement", "जमिनीवरील जमिनीखालील"],
        "mr": "हे विशिष्ट पिकाच्या  'वाढीच्या मॉडेल'वर आधारित AI अल्गोरिदमद्वारे  उपग्रह डेटाचे विश्लेषण करून  अंदाजित  केले जाते.",
        "hi": "यह विशिष्ट फसल के  'विकास मॉडल' पर आधारित AI एल्गोरिदम  द्वारा उपग्रह डेटा का विश्लेषण करके  अनुमानित  किया जाता है।",
        "en": "This is  estimated  by  AI algorithms based on the specific crop's 'growth model'  by analyzing satellite data."
    },
    "stress_events_zero": {
        "keywords": ["स्ट्रेस इव्हेंट्स शून्य आहेत", "stress events zero", "तनाव घटनाएं शून्य"],
        "mr": "शून्य 'स्ट्रेस इव्हेंट्स' म्हणजे सध्या कोणतेही मोठे धोके नाहीत. तथापि, 'ग्रोथ इंडेक्स' स्थिर किंवा कमी होत असल्यास,  सूक्ष्म कमतरता (Micro-Deficiency)  असू शकते.",
        "hi": "शून्य 'तनाव घटनाओं' का मतलब है कि वर्तमान में कोई बड़ा खतरा नहीं है। हालांकि, यदि 'ग्रोथ इंडेक्स' स्थिर या कम हो रहा है, तो  सूक्ष्म कमी (Micro-Deficiency)  हो सकती है।",
        "en": "Zero 'Stress Events' means there are no major risks currently. However, if the 'Growth Index' is stable or decreasing, there might be a  Micro-Deficiency ."
    },
    "recovery_rate_low_comparison": {
        "keywords": ["रिकव्हरी रेट कमी का", "recovery rate low reason", "रिकवरी रेट कम क्यों"],
        "mr": "'रिकव्हरी रेट' साखरेच्या गुणवत्तेवर आणि जातीवर अवलंबून असतो. जरी तो प्रादेशिक सरासरीपेक्षा चांगला असला तरी, तो अजूनही  'इष्टतम पातळी' (Optimal Level) पर्यंत पोहोचलेला नाही .",
        "hi": "'रिकवरी रेट' चीनी की गुणवत्ता और किस्म पर निर्भर करता है। भले ही यह क्षेत्रीय औसत से बेहतर हो, यह अभी भी  'इष्टतम स्तर' (Optimal Level) तक नहीं पहुंचा है ।",
        "en": "The 'Recovery Rate' depends on sugar quality and variety. Even if it is better than the regional average, it still  hasn't reached the 'Optimal Level' ."
    },
    "recovery_rate_improve_potash": {
        "keywords": ["रिकव्हरी रेट सुधारण्यासाठी उपाय", "improve recovery rate", "पोटॅश", "potash"],
        "mr": "'रिकव्हरी रेट' वाढवण्यासाठी पिकाच्या योग्य टप्प्यावर  पोटॅश (Potash) आणि सल्फर (Sulphur)  सारख्या पोषक तत्वांचा योग्य प्रमाणात वापर करणे महत्त्वाचे आहे.",
        "hi": "'रिकवरी रेट' बढ़ाने के लिए फसल के सही चरण में  पोटाश (Potash) और सल्फर (Sulphur)  जैसे पोषक तत्वों का सही मात्रा में उपयोग करना महत्वपूर्ण है।",
        "en": "To increase the 'Recovery Rate', it is important to use the right amount of nutrients like  Potash and Sulphur  at the appropriate crop stage."
    },
    "biomass_decrease_causes": {
        "keywords": ["बायोमास कमी होऊ शकतो", "biomass decrease causes", "बायोमास कम होने के कारण"],
        "mr": " पाण्याचा ताण, पोषक तत्वांची कमतरता , अपुरा सूर्यप्रकाश किंवा रोग/कीटकांचा प्रादुर्भाव यांमुळे 'बायोमास' कमी होऊ शकतो.",
        "hi": " पानी का तनाव, पोषक तत्वों की कमी , अपर्याप्त धूप या रोग/कीटों का प्रकोप के कारण 'बायोमास' कम हो सकता है।",
        "en": "'Biomass' can decrease due to  water stress, nutrient deficiency , insufficient sunlight, or pest/disease infestation."
    },
    "soil_ph_nutrient_relation": {
        "keywords": ["pH पोषक तत्वांची उपलब्धता", "ph nutrient relation", "pH और पोषक तत्व"],
        "mr": "मातीचा pH योग्य असल्यास (उदा. ६.५ ते ७.५),  नायट्रोजन, फॉस्फरस आणि पोटॅशसह बहुतेक पोषक तत्त्वे  पिकांसाठी सहज उपलब्ध होतात. pH बदलल्यास उपलब्धता कमी होते.",
        "hi": "यदि मिट्टी का pH सही है (जैसे ६.५ से ७.५), तो  नाइट्रोजन, फास्फोरस और पोटाश सहित अधिकांश पोषक तत्व  फसलों के लिए आसानी से उपलब्ध होते हैं। pH बदलने पर उपलब्धता कम हो जाती है।",
        "en": "If the soil pH is correct (e.g., 6.5 to 7.5),  most nutrients, including Nitrogen, Phosphorus, and Potash , are readily available to crops. Availability decreases if the pH changes."
    },
    # ----------------------------------------------------------------------
    # ४. उत्पादन आणि कार्यक्षमता (Yield & Performance) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "projected_vs_optimal_yield": {
        "keywords": ["प्रोजेक्टेड यील्ड कमी का", "projected vs optimal yield", "उत्पादन अनुमान कम क्यों"],
        "mr": "'प्रोजेक्टेड यील्ड' तुमच्या सध्याच्या व्यवस्थापन आणि वाढीच्या स्थितीवर आधारित आहे, तर 'ऑप्टिमल यील्ड' हे  सर्वात चांगल्या परिस्थितीत  शक्य असलेले उत्पादन आहे.",
        "hi": "'प्रोजेक्टेड यील्ड' आपके वर्तमान प्रबंधन और वृद्धि की स्थिति पर आधारित है, जबकि 'ऑप्टिमल यील्ड'  सर्वोत्तम परिस्थितियों  में संभव उत्पादन है।",
        "en": "'Projected Yield' is based on your current management and growth status, while 'Optimal Yield' is the production possible under  the best possible conditions ."
    },
    "optimal_yield_management_changes": {
        "keywords": ["ऑप्टिमल यील्ड पर्यंत पोहोचण्यासाठी", "optimal yield management changes", "सर्वोत्तम उत्पादन के लिए"],
        "mr": " सिंचन, खतांचे वेळापत्रक आणि योग्य जातीची निवड  सुधारून, तसेच तणावाचे प्रमाण कमी करून हे बदल करता येतात.",
        "hi": " सिंचाई, उर्वरक अनुसूची और सही किस्म के चयन  में सुधार करके, साथ ही तनाव की मात्रा को कम करके ये बदलाव किए जा सकते हैं।",
        "en": "These changes can be made by improving  irrigation, fertilizer scheduling, and selection of the right variety , as well as reducing the amount of stress."
    },
    "performance_action_plan": {
        "keywords": ["परफॉर्मन्स वाढवण्यासाठी कृती योजना", "performance action plan", "कार्यक्षमता बढ़ाने के लिए"],
        "mr": "पुढील तीन महिन्यांसाठी 'ग्रोथ इंडेक्स' सुधारण्यासाठी  खतांचा आणि पाण्याची गरज पूर्ण करणारी शिफारस केलेली कृती योजना  (Recommended Action Plan) वापरावी.",
        "hi": "अगले तीन महीनों के लिए 'ग्रोथ इंडेक्स' में सुधार के लिए  खाद और पानी की जरूरतें पूरी करने वाली अनुशंसित कार्य योजना  (Recommended Action Plan) का उपयोग करें।",
        "en": "Use the  Recommended Action Plan  that meets the fertilizer and water needs to improve the 'Growth Index' for the next three months."
    },
    "low_yield_high_recovery": {
        "keywords": ["रिकव्हरी रेट चांगला असूनही उत्पादन कमी", "high recovery low yield", "रिकवरी रेट अच्छा फिर भी"],
        "mr": "'रिकव्हरी रेट' (गुणवत्ता) चांगला असला तरी, तुमचा  'एकूण बायोमास' कमी  असेल, तर एकूण उत्पादन (Total Quantity) कमीच राहील.",
        "hi": "'रिकवरी रेट' (गुणवत्ता) अच्छा होने के बावजूद, यदि आपका  'कुल बायोमास' कम  है, तो कुल उत्पादन (Total Quantity) कम ही रहेगा।",
        "en": "Even if the 'Recovery Rate' (quality) is good, if your  'Total Biomass' is low , the total yield (Total Quantity) will remain low."
    },
    "yield_increase_irrigation_vs_fertilizer": {
        "keywords": ["उत्पादन वाढवण्यासाठी सिंचन की खते", "irrigation vs fertilizer for yield", "सिंचाई या खाद"],
        "mr": "प्रथम  'वॉटर इंडेक्स' आणि 'ग्रोथ इंडेक्स' तपासा . जर दोन्ही कमी असतील, तर दोन्ही आवश्यक आहेत. फक्त ग्रोथ कमी असेल तर खत आवश्यक आहे.",
        "hi": "पहले  'वॉटर इंडेक्स' और 'ग्रोथ इंडेक्स' जांचें । यदि दोनों कम हैं, तो दोनों आवश्यक हैं। यदि केवल ग्रोथ कम है तो खाद आवश्यक है।",
        "en": "First,  check the 'Water Index' and 'Growth Index' . If both are low, both are necessary. If only Growth is low, fertilizer is necessary."
    },
    "yield_projection_accuracy": {
        "keywords": ["यील्ड प्रोजेक्शनची अचूकता", "yield projection accuracy", "उत्पादन अनुमान की सटीकता"],
        "mr": "हे AI मॉडेलची अचूकता (Accuracy)  ९०% किंवा त्याहून अधिक  असते, परंतु हवामानातील मोठे आणि अनपेक्षित बदल या अंदाजावर परिणाम करू शकतात.",
        "hi": "इस AI मॉडल की सटीकता (Accuracy)  ९०% या उससे अधिक  होती है, परंतु मौसम में बड़े और अप्रत्याशित बदलाव इस अनुमान को प्रभावित कर सकते हैं।",
        "en": "The accuracy of this AI model is  90% or higher , but large and unexpected changes in weather can affect this prediction."
    },
    "low_yield_area_map": {
        "keywords": ["उत्पादन कमी येण्याची शक्यता नकाशावर", "low yield area map", "कम उत्पादन वाला क्षेत्र"],
        "mr": "होय, CropEye.ai  'झोन मॅनेजमेंट' (Zone Management) नकाशावर  'ग्रोथ इंडेक्स' सर्वात कमी असलेल्या भागांना चिन्हांकित करून दाखवते, जिथे उत्पादन कमी असेल.",
        "hi": "हाँ, CropEye.ai  'ज़ोन मैनेजमेंट' (Zone Management) मानचित्र  पर 'ग्रोथ इंडेक्स' सबसे कम वाले क्षेत्रों को चिह्नित करके दिखाता है, जहाँ उत्पादन कम होगा।",
        "en": "Yes, CropEye.ai shows areas with the lowest 'Growth Index' by marking them on the  'Zone Management' map , indicating where the yield will be low."
    },
    # ----------------------------------------------------------------------
    # ५. कृती आणि निर्णय समर्थन (Action & Decision Support) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "irrigation_event_impact": {
        "keywords": ["सिंचन इव्हेंट्स वॉटर इंडेक्सवर परिणाम", "irrigation events water index impact", "सिंचाई का प्रभाव"],
        "mr": "सिंचन इव्हेंट्स वाढवल्यास  'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' लगेच वाढतात , ज्यामुळे पिकाचा ताण कमी होतो.",
        "hi": "सिंचन इव्हेंट्स वाढवल्यास  'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' लगेच वाढतात , ज्यामुळे पिकाचा ताण कमी होतो.",
        "en": "Increasing irrigation events  immediately raises the 'Water Index' and 'Moisture Index' , which reduces crop stress."
    },
    "weather_forecast_irrigation_planning": {
        "keywords": ["७ दिवसांच्या हवामान अंदाजानुसार सिंचन नियोजन", "weather forecast irrigation planning", "मौसम अनुमान सिंचाई"],
        "mr": "जर पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "hi": "यदि पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "en": "If heavy rain is forecast in the next 48 hours,  stop irrigation . If the temperature is going to rise, increase the amount of irrigation."
    },
    "file_report_records": {
        "keywords": ["फाइल रिपोर्ट मध्ये नोंदी", "file report records", "फाइल रिपोर्ट में रिकॉर्ड"],
        "mr": "तुम्ही  खतांचा वापर, फवारणी, सिंचनाच्या वेळा, मजुरीचा खर्च  आणि इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "hi": "आप  खाद का उपयोग, छिड़काव, सिंचाई का समय, मजदूरी का खर्च  और इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "en": "You can keep records of  fertilizer usage, spraying, irrigation times, labor costs , and all other farm activities."
    },
    "sales_report_impact": {
        "keywords": ["सेल्स रिपोर्ट भरल्याने फरक", "sales report impact", "बिक्री रिपोर्ट का प्रभाव"],
        "mr": "'सेल्स रिपोर्ट' थेट डॅशबोर्डवरील डेटा (उदा. इंडेक्स) बदलत नाही, परंतु तुमच्या  आर्थिक अहवालावर (Financial Report)  आणि उत्पादन विश्लेषणामध्ये (Yield Analysis) मदत करतो.",
        "hi": "'सेल्स रिपोर्ट' थेट डॅशबोर्डवरील डेटा (उदा. इंडेक्स) बदलत नाही, परंतु तुमच्या  आर्थिक अहवालावर (Financial Report)  आणि उत्पादन विश्लेषणामध्ये (Yield Analysis) मदत करतो.",
        "en": "The 'Sales Report' does not directly change the data on the dashboard (e.g., indices), but it helps with your  Financial Report  and Yield Analysis."
    },
    "dashboard_alerts_phone": {
        "keywords": ["सूचना फोनवर मेसेजद्वारे", "dashboard alerts phone", "अलर्ट मैसेज"],
        "mr": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "hi": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "en": "Yes, the CropEye.ai app allows you to send important Alerts like  'Irrigation Need'  or  'Stress Risk'  directly to your phone via message or notification."
    },
    "historical_data_comparison": {
        "keywords": ["मागील वर्षाच्या डेटा सोबत तुलना", "historical data comparison", "पिछले साल का डेटा"],
        "mr": "डॅशबोर्डवर  'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "hi": "डॅशबोर्डवर  'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "en": "You can compare the Growth Index, Stress Index, and Yield Projection by selecting the  'Yearly' or 'Comparison'  option on the dashboard."
    },
    "fertilizer_recommendation": {
        "keywords": ["कोणत्या विशिष्ट खतांची गरज", "fertilizer recommendation NPK", "खाद की सिफारिश"],
        "mr": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "hi": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "en": "Yes, by analyzing the 'Growth Index' and soil pH level, the dashboard recommends  NPK and Micro-Nutrients ."
    },
    "recovery_rate_advisor": {
        "keywords": ["रिकव्हरी रेट कमी असल्यास कृषी सल्लागार", "recovery rate advisor", "कृषि सलाहकार"],
        "mr": "'रिकव्हरी रेट' (साखरेची गुणवत्ता) सुधारण्यासाठी तुम्हाला  ऊस पिकातील पोषण आणि व्यवस्थापनाचा अनुभव  असलेल्या कृषी तज्ञाची मदत घ्यावी लागेल.",
        "hi": "'रिकव्हरी रेट' (साखरेची गुणवत्ता) सुधारण्यासाठी तुम्हाला  ऊस पिकातील पोषण आणि व्यवस्थापनाचा अनुभव  असलेल्या कृषी तज्ञाची मदत घ्यावी लागेल.",
        "en": "To improve the 'Recovery Rate' (sugar quality), you will need the help of an agricultural expert who has  experience in nutrition and management of sugarcane crops ."
    },
    # ----------------------------------------------------------------------
    # नवीन डॅशबोर्ड कंपोनंट्सची माहिती Q&A म्हणून जोडत आहोत (Dashboard Components Benefits)
    # ----------------------------------------------------------------------
    "field_area_benefit": {
        "keywords": ["फील्ड एरिया फायदा", "field area benefit", "क्षेत्रफल लाभ"],
        "mr": "फील्ड एरियामुळे पेरणी, खत आणि सिंचन यासाठी  प्रति एकर खर्चाचे अचूक आणि सोपे नियोजन  करता येते.",
        "hi": "फील्ड एरियामुळे पेरणी, खत आणि सिंचन यासाठी  प्रति एकर खर्चाचे अचूक आणि सोपे नियोजन  करता येते.",
        "en": "Field Area allows for  accurate and easy planning of cost per acre  for planting, fertilizer, and irrigation."
    },
    "crop_status_benefit": {
        "keywords": ["पीक स्थिती फायदा", "crop status benefit", "फसल स्थिति लाभ"],
        "mr": "पीक स्थितीमुळे पिकाच्या गरजेनुसार व्यवस्थापनाचे निर्णय (उदा. फवारणी, पाणी थांबवणे) घेण्यासाठी  वेळेची अचूकता  मिळते.",
        "hi": "पीक स्थितीमुळे पिकाच्या गरजेनुसार व्यवस्थापनाचे निर्णय (उदा. फवारणी, पाणी थांबवणे) घेण्यासाठी  वेळेची अचूकता  मिळते.",
        "en": "Crop Status provides  timing accuracy  for making management decisions (e.g., spraying, stopping water) according to the crop's needs."
    },
    "days_to_harvest_benefit": {
        "keywords": ["कापणीसाठीचे दिवस फायदा", "days to harvest benefit", "कटाई के दिन लाभ"],
        "mr": "कापणीच्या दिवसांमुळे मजूर, वाहतूक आणि विक्रीचे नियोजन वेळेवर सुरू करून  काढणीची प्रक्रिया सुलभ  करता येते.",
        "hi": "कापणीच्या दिवसांमुळे मजूर, वाहतूक आणि विक्रीचे नियोजन वेळेवर सुरू करून  काढणीची प्रक्रिया सुलभ  करता येते.",
        "en": "Days to Harvest allows  simplification of the harvesting process  by starting timely planning for labor, transport, and sales."
    },
    "sugar_content_benefit": {
        "keywords": ["साखर सामग्री फायदा", "sugar content benefit", "चीनी की सामग्री लाभ"],
        "mr": "साखर सामग्रीमुळे सर्वात योग्य वेळी कापणीचा निर्णय घेणे, जेणेकरून कारखान्यात ऊस पाठवल्यावर  जास्तीत जास्त रिकव्हरी  मिळेल.",
        "hi": "साखर सामग्रीमुळे सर्वात योग्य वेळी कापणीचा निर्णय घेणे, जेणेकरून कारखान्यात ऊस पाठवल्यावर  जास्तीत जास्त रिकव्हरी  मिळेल.",
        "en": "Sugar Content allows the decision for harvest at the most appropriate time, ensuring  maximum recovery  when sending sugarcane to the factory."
    },
    "indices_snapshot_benefit": {
        "keywords": ["इंडायसेस झलक फायदा", "indices snapshot benefit", "सूचकांक लाभ"],
        "mr": "फील्ड इंडायसेसमुळे पिकाचे आरोग्य एका दृष्टिक्षेपात समजते आणि खत, पाणी किंवा तणाव यापैकी  कोणती समस्या आहे हे त्वरित कळते .",
        "hi": "फील्ड इंडायसेसमुळे पिकाचे आरोग्य एका दृष्टिक्षेपात समजते आणि खत, पाणी किंवा तणाव यापैकी  कोणती समस्या आहे हे त्वरित कळते ।",
        "en": "Field Indices allow quick understanding of crop health and immediate identification of whether the problem is fertilizer, water, or stress-related."
    },
    "organic_carbon_density_benefit": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी फायदा", "organic carbon benefit", "सेंद्रिय कर्ब लाभ"],
        "mr": "ऑरगॅनिक कार्बन डेन्सिटीमुळे जमिनीची सुपीकता सुधारण्यासाठी  सेंद्रिय खते आणि पीक अवशेष व्यवस्थापनाचे निर्णय  घेण्यासाठी आधार मिळतो.",
        "hi": "ऑरगॅनिक कार्बन डेन्सिटीमुळे जमिनीची सुपीकता सुधारण्यासाठी  सेंद्रिय खते आणि पीक अवशेष व्यवस्थापनाचे निर्णय  घेण्यासाठी आधार मिळतो।",
        "en": "Organic Carbon Density provides the basis for making  decisions on organic fertilizers and crop residue management  to improve soil fertility."
    },
    "stress_events_benefit": {
        "keywords": ["तणाव घटना फायदा", "stress events benefit", "तनाव घटनाएं लाभ"],
        "mr": "तणाव घटनांमुळे जोखीम कमी करण्यासाठी (Risk Mitigation) आणि भविष्यात तणाव टाळण्यासाठी  व्यवस्थापनात सुधारणा  करणे शक्य होते.",
        "hi": "तणाव घटनांमुळे जोखीम कमी करण्यासाठी (Risk Mitigation) आणि भविष्यात तणाव टाळण्यासाठी  व्यवस्थापनात सुधारणा  करणे शक्य होते।",
        "en": "Stress Events enable  improvement in management  to mitigate risk and prevent stress in the future."
    },
    "soil_ph_level_benefit": {
        "keywords": ["मातीचा pH स्तर फायदा", "soil ph benefit", "pH स्तर लाभ"],
        "mr": "मातीचा pH स्तर योग्य असल्यास आवश्यकतेनुसार माती सुधारक (उदा. चुना, जिप्सम) वापरून  पोषक तत्वांची उपलब्धता वाढवता येते .",
        "hi": "मातीचा pH स्तर योग्य असल्यास आवश्यकतेनुसार माती सुधारक (उदा. चुना, जिप्सम) वापरून  पोषक तत्वांची उपलब्धता वाढवता येते ।",
        "en": "When the soil pH level is correct, the availability of nutrients can be increased by using soil amendments (e.g., lime, gypsum) as needed."
    },
    "yield_projection_benefit": {
        "keywords": ["उत्पादन अंदाज फायदा", "yield projection benefit", "उत्पादन अनुमान लाभ"],
        "mr": "उत्पादन अंदाजामुळे बाजारातील धोरणे (Market Strategy) लवकर निश्चित करून  चांगला दर मिळवण्याचा प्रयत्न  करणे शक्य होते.",
        "hi": "उत्पादन अंदाजामुळे बाजारातील धोरणे (Market Strategy) लवकर निश्चित करून  चांगला दर मिळवण्याचा प्रयत्न  करणे शक्य होते।",
        "en": "Yield Projection allows for early determination of market strategies to  attempt to get a better price ."
    },
    "recovery_rate_comparison_benefit": {
        "keywords": ["रिकव्हरी रेट तुलना फायदा", "recovery rate comparison benefit", "रिकवरी रेट तुलना लाभ"],
        "mr": "रिकव्हरी रेट तुलना केल्याने तुमचा साखर गुणवत्ता दर सरासरीपेक्षा चांगला आहे की नाही हे समजते, ज्यामुळे  व्यवस्थापन सुधारण्यास मदत  होते.",
        "hi": "रिकव्हरी रेट तुलना केल्याने तुमचा साखर गुणवत्ता दर सरासरीपेक्षा चांगला आहे की नाही हे समजते, ज्यामुळे  व्यवस्थापन सुधारण्यास मदत  होते।",
        "en": "Recovery Rate Comparison helps determine if your sugar quality rate is better than the average, which  helps improve management ."
    },
    "data_source": {
        "keywords": ["data source", "डेटा कुठून येतो", "माहितीचे स्रोत", "data kahan se aata hai", "source of information"],
        "mr": "माहिती प्रामुख्याने  उपग्रह प्रतिमा (Satellite Imagery) ,  हवामान डेटा (Weather Data) ,  शेतकऱ्यांनी भरलेला ग्राउंड डेटा  आणि  AI ॲनालिसिस मॉडेल  मधून येते.",
        "hi": "जानकारी मुख्य रूप से  उपग्रह छवियों (Satellite Imagery) ,  मौसम डेटा ,  किसानों द्वारा भरे गए ग्राउंड डेटा  और  AI एनालिसिस मॉडल  से आती है।",
        "en": "The data primarily comes from  Satellite Imagery ,  Weather Data ,  Ground Data  fed by farmers, and  AI analysis models ."
    },
    "crop_suitability": {
        "keywords": ["कोणत्या पिकांसाठी योग्य", "which crops are supported", "किसानों फसलें", "ऊस", "sugarcane", "धान्य"],
        "mr": "CropEye.ai हे ऊसासारख्या (Sugarcane)  दीर्घकालीन पिकांसाठी आणि  धान्य, कापूस  यांसारख्या अनेक प्रमुख पिकांसाठी डिझाइन केलेले आहे.",
        "hi": "CropEye.ai  गन्ने (Sugarcane)  जैसी लंबी अवधि की फसलों और  अनाज, कपास  जैसी कई प्रमुख फसलों के लिए डिज़ाइन किया गया है।",
        "en": "CropEye.ai is designed for long-duration crops like  Sugarcane , as well as many major crops like  cereals and cotton ."
    },
    # ----------------------------------------------------------------------
    # २. फील्ड इंडायसेस (Field Indices) आणि पिकाचे आरोग्य
    # ----------------------------------------------------------------------
    "growth_index_low_reason": {
        "keywords": ["ग्रोथ इंडेक्स कमी का", "growth index low reason", "ग्रोथ इंडेक्स कम क्यों","growth"],
        "mr": "'ग्रोथ इंडेक्स' कमी होण्याची मुख्य कारणे म्हणजे  पाण्याची कमतरता , पोषक तत्वांची (उदा. नायट्रोजन) कमतरता किंवा पिकावर आलेला  ताण (Stress) .",
        "hi": "'ग्रोथ इंडेक्स' कम होने के मुख्य कारण  पानी की कमी , पोषक तत्वों की कमी या फसल पर आया हुआ  तनाव (Stress)  हैं।",
        "en": "The main reasons for a low 'Growth Index' are  water deficit , lack of nutrients (e.g., Nitrogen), or  stress  on the crop."
    },
    "growth_index_optimal_level": {
        "keywords": ["ग्रोथ इंडेक्स कोणत्या पातळीवर", "growth index optimal level", "ग्रोथ इंडेक्स स्तर", "योग्य NDVI"],
        "mr": "पिकाच्या प्रकारानुसार आणि टप्प्यानुसार ही पातळी बदलते, परंतु शक्यतो हा निर्देशांक  ०.७५ ते ०.९०  दरम्यान आणि स्थिर राखणे फायदेशीर असते.",
        "hi": "फसल के प्रकार और चरण के अनुसार यह स्तर बदलता है, लेकिन इसे  ०.७५ से ०.९०  के बीच और स्थिर बनाए रखना फायदेमंद होता है।",
        "en": "The optimal Growth Index level usually ranges between  0.75 and 0.90 , depending on the crop and its growth stage."
    },
    "stress_index_high_first_step": {
        "keywords": ["स्ट्रेस इंडेक्स वाढल्यास उपाययोजना", "stress index high first step","stress", "स्ट्रेस इंडेक्स उपाय", "तणाव वाढला"],
        "mr": "'स्ट्रेस इंडेक्स' वाढल्यास प्रथम  मातीतील ओलावा तपासावा . पाण्याची कमतरता असल्यास  त्वरित सिंचन  सुरू करावे; नसेल तर रोगतज्ज्ञांचा सल्ला घ्यावा.",
        "hi": "'स्ट्रेस इंडेक्स' बढ़ने पर, सबसे पहले  मिट्टी की नमी जांचें । पानी की कमी होने पर  तुरंत सिंचाई  शुरू करें; अन्यथा, रोग विशेषज्ञ से सलाह लें।",
        "en": "If the 'Stress Index' is high, first  check the soil moisture . If there's a water deficit,  start irrigation immediately ; otherwise, consult a pathologist."
    },
    "stress_index_disease_detection": {
        "keywords": ["स्ट्रेस इंडेक्स रोग ओळखू शकतो", "stress index disease detection", "रोग पहचान", "disease detection"],
        "mr": "'स्ट्रेस इंडेक्स'  रोगांमुळे आलेला ताण  (उदा. बुरशीजन्य रोग) ओळखू शकतो, परंतु विशिष्ट रोगाचे नाव देण्यासाठी शेतकऱ्यांनी ग्राउंड व्हिजिट करणे आवश्यक आहे.",
        "hi": "'स्ट्रेस इंडेक्स'  रोगों के कारण हुए तनाव  (जैसे फंगल रोग) को पहचान सकता है, लेकिन विशिष्ट रोग का नाम बताने के लिए किसानों को ग्राउंड विज़िट करना आवश्यक है।",
        "en": "The 'Stress Index' can identify  stress caused by diseases  (e.g., fungal diseases), but farmers need to conduct a ground visit to name the specific disease."
    },
    "growth_index_low_fertilizer": {
        "keywords": ["ग्रोथ इंडेक्स सुधारणा खत", "","growth index fertilizer", "ग्रोथ इंडेक्स खाद", "युरिया", "नाइट्रोजन"],
        "mr": "ग्रोथ इंडेक्स थेट  नायट्रोजनच्या कमतरतेशी  संबंधित असतो. त्यामुळे नायट्रोजनयुक्त खत (उदा. युरिया) त्वरित देण्याची शिफारस केली जाते.",
        "hi": "ग्रोथ इंडेक्स सीधे  नाइट्रोजन की कमी  से संबंधित होता है। इसलिए, नाइट्रोजन युक्त खाद (जैसे यूरिया) तुरंत देने की सिफारिश की जाती है।",
        "en": "The Growth Index is directly linked to  Nitrogen deficiency . Immediate application of Nitrogen-rich fertilizer (e.g., Urea) is recommended."
    },
    # ----------------------------------------------------------------------
    # ३. जल व्यवस्थापन (Water Management)
    # ----------------------------------------------------------------------
    "water_vs_moisture_index": {
        "keywords": ["वॉटर इंडेक्स मॉईश्चर इंडेक्स फरक", "water moisture index difference","water", "पानी और नमी सूचकांक", "पानांमधील पाणी"],
        "mr": " 'वॉटर इंडेक्स'  पिकाच्या  पानांमधील पाण्याची मात्रा  दर्शवतो, तर  'मॉईश्चर इंडेक्स'   मातीतील ओलाव्याचे प्रमाण  दर्शवतो.",
        "hi": " 'वॉटर इंडेक्स'  फसल की  पत्तियों में पानी की मात्रा  दर्शाता है, जबकि  'मॉइश्चर इंडेक्स'   मिट्टी की नमी की मात्रा  दर्शाता है।",
        "en": "The  'Water Index'  shows the  amount of water in the crop leaves , while the  'Moisture Index'  shows the  amount of moisture in the soil ."
    },
    "moisture_index_irrigation_level": {
        "keywords": ["मॉईश्चर इंडेक्स सिंचन पातळी", "moisture","moisture index irrigation level", "नमी सूचकांक सिंचाई", "किती झाल्यावर पाणी द्यावे"],
        "mr": "जेव्हा 'मॉईश्चर इंडेक्स'  ५०% च्या खाली  जातो, तेव्हा  त्वरित सिंचनाची  शिफारस केली जाते.",
        "hi": "जब 'मॉइश्चर इंडेक्स'  ५०% से नीचे  चला जाता है, तब  तुरंत सिंचाई  करने की सिफारिश की जाती है।",
        "en": "When the 'Moisture Index' drops  below 50% ,  immediate irrigation  is recommended."
    },
    "irrigation_schedule_change": {
        "keywords": ["सिंचन वेळापत्रक आपोआप बदलते", "paani","pani","irrigation schedule auto change", "सिंचाई का समय", "schedule badalta hai"],
        "mr": "होय, CropEye.ai चे 'इरिगेशन शेड्यूल' पिकाच्या टप्प्यांमध्ये पाण्याच्या गरजेनुसार आणि  हवामान बदलांनुसार  आपोआप बदलले जाते.",
        "hi": "हाँ, CropEye.ai का 'सिंचाई शेड्यूल' फसल के चरणों में पानी की आवश्यकता और  मौसम के बदलावों के अनुसार  स्वचालित रूप से बदल जाता है।",
        "en": "Yes, CropEye.ai's 'Irrigation Schedule' is automatically adjusted according to the water needs during the crop stages and  weather changes ."
    },
    "water_index_no_improvement": {
        "keywords": ["सिंचन केल्यावरही वॉटर इंडेक्स सुधारत नाही", "water index","water index no improvement", "सिंचाई के बाद भी सुधार नहीं"],
        "mr": "याचा अर्थ मुळांना पाणी शोषण्यात अडचण येत आहे. हे कदाचित  माती घट्ट झाल्यामुळे (Compaction)  किंवा मुळांना रोग झाल्यामुळे असू शकते.",
        "hi": "इसका मतलब है कि जड़ों को पानी सोखने में दिक्कत आ रही है। यह शायद  मिट्टी के सख्त होने (Compaction)  या जड़ों में रोग होने के कारण हो सकता है।",
        "en": "This means the roots are having trouble absorbing water. This may be due to  soil compaction  or root diseases."
    },
    "weather_forecast_irrigation_planning": {
        "keywords": ["७ दिवसांच्या हवामान अंदाजानुसार सिंचन नियोजन","weather", "weather forecast irrigation planning", "मौसम अनुमान सिंचाई", "पावसाचा अंदाज"],
        "mr": "जर पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "hi": "यदि अगले ४८ घंटों में भारी बारिश का अनुमान है, तो  सिंचाई रोक दें । यदि तापमान बढ़ने वाला है, तो सिंचाई की मात्रा बढ़ा दें।",
        "en": "If heavy rain is forecast in the next 48 hours,  stop irrigation . If the temperature is going to rise, increase the amount of irrigation."
    },
    # ----------------------------------------------------------------------
    # ४. माती आणि पोषण व्यवस्थापन (Soil & Nutrition Management)
    # ----------------------------------------------------------------------
    "organic_carbon_optimal": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी किती", "organic carbon optimal level", "सेंद्रिय कर्ब", "oc","soil","organic carbon density"],
        "mr": "साधारणपणे, सेंद्रिय कर्बाचे प्रमाण  ०.५% पेक्षा जास्त  (म्हणजेच gm/cm³ मध्ये जास्त) असल्यास मातीची गुणवत्ता चांगली मानली जाते.",
        "hi": "सामान्यतः, यदि कार्बनिक कार्बन की मात्रा  ०.५% से अधिक  है तो मिट्टी की गुणवत्ता अच्छी मानी जाती है।",
        "en": "Generally, soil quality is considered good if the organic carbon content is  greater than 0.5% ."
    },
    "organic_carbon_improve": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी सुधारण्यासाठी खत", "improve organic carbon", "oc","सेंद्रिय खत", "कंपोस्ट"],
        "mr": " शेणखत, कंपोस्ट खत, गांडूळ खत  किंवा हिरवळीची खते (Green Manure) वापरून 'ऑरगॅनिक कार्बन डेन्सिटी' सुधारता येते.",
        "hi": " गोबर की खाद, कंपोस्ट खाद, केंचुआ खाद  या हरी खाद (Green Manure) का उपयोग करके 'कार्बनिक कार्बन घनत्व' में सुधार किया जा सकता है।",
        "en": " Cow dung manure, compost, vermicompost,  or green manures can be used to improve 'Organic Carbon Density'."
    },
    "soil_ph_sugarcane_optimal": {
        "keywords": ["pH लेव्हल ऊस पिकासाठी योग्य आहे", "soil ph level sugarcane", "pH 7.30", "मातीचा पीएच"],
        "mr": " ७.३० pH  ऊस पिकासाठी स्वीकार्य आहे (ऊस ६.० ते ८.५ pH मध्ये वाढतो). pH जास्त असल्यास  गंधक (Sulphur)  वापरावा आणि कमी असल्यास  चुना (Lime)  वापरावा.",
        "hi": " ७.३० pH  गन्ने की फसल के लिए स्वीकार्य है। pH अधिक होने पर  सल्फर (Sulphur)  का उपयोग करें और कम होने पर  चूना (Lime)  का उपयोग करें।",
        "en": " 7.30 pH  is acceptable for sugarcane. Use  Sulphur  if the pH is high and  Lime  if it is low."
    },
    "fertilizer_recommendation": {
        "keywords": ["कोणत्या विशिष्ट खतांची गरज", "fertilizer recommendation NPK", "खाद की सिफारिश", "NPK", "सूक्ष्म पोषक तत्व"],
        "mr": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "hi": "हाँ, 'ग्रोथ इंडेक्स' और मिट्टी pH स्तर का विश्लेषण करके डॅशबोर्ड  NPK और सूक्ष्म पोषक तत्वों (Micro-Nutrients)  की सिफारिश करता है।",
        "en": "Yes, by analyzing the 'Growth Index' and soil pH level, the dashboard recommends  NPK and Micro-Nutrients ."
    },
    "soil_ph_nutrient_relation": {
        "keywords": ["pH पोषक तत्वांची उपलब्धता", "ph nutrient relation", "pH और पोषक तत्व", "nutrient availability"],
        "mr": "मातीचा pH योग्य असल्यास (उदा. ६.५ ते ७.५),  नायट्रोजन, फॉस्फरस आणि पोटॅशसह बहुतेक पोषक तत्त्वे  पिकांसाठी सहज उपलब्ध होतात. pH बदलल्यास उपलब्धता कमी होते.",
        "hi": "यदि मिट्टी का pH सही है (जैसे ६.५ से ७.५), तो  नाइट्रोजन, फास्फोरस और पोटाश सहित अधिकांश पोषक तत्व  फसलों के लिए आसानी से उपलब्ध होते हैं।",
        "en": "If the soil pH is correct (e.g., 6.5 to 7.5),  most nutrients, including NPK , are readily available to crops. Availability decreases if the pH changes."
    },
    # ----------------------------------------------------------------------
    # ५. उत्पादन आणि कापणी (Yield & Harvest Management)
    # ----------------------------------------------------------------------
    "projected_vs_optimal_yield": {
        "keywords": ["प्रोजेक्टेड यील्ड कमी का", "projected vs optimal yield", "उत्पादन अंदाज कम क्यों", "optimal yield"],
        "mr": "'प्रोजेक्टेड यील्ड' तुमच्या सध्याच्या व्यवस्थापनावर आधारित आहे, तर 'ऑप्टिमल यील्ड' हे  सर्वात चांगल्या परिस्थितीत  शक्य असलेले उत्पादन आहे. व्यवस्थापन सुधारून तुम्ही ऑप्टिमल यील्ड गाठू शकता.",
        "hi": "'प्रोजेक्टेड यील्ड' आपके वर्तमान प्रबंधन पर आधारित है, जबकि 'ऑप्टिमल यील्ड'  सर्वोत्तम परिस्थितियों  में संभव उत्पादन है। प्रबंधन में सुधार करके आप ऑप्टिमल यील्ड तक पहुँच सकते हैं।",
        "en": "'Projected Yield' is based on your current management, while 'Optimal Yield' is the production possible under  the best possible conditions . You can reach optimal yield by improving management."
    },
    "sugar_content_harvest": {
        "keywords": ["साखर कंटेंट कापणी", "sugar content harvest", "शुगर कंटेंट", "रिकव्हरी मिळेल", "brix"],
        "mr": "ऊस पिकासाठी, साखरेचा  'सरासरी ब्रिक्स' (Avg Brix)  जेव्हा विशिष्ट पातळीपेक्षा जास्त (उदा. १९-२०) होतो, तेव्हा कापणीसाठी तोडगा काढणे फायदेशीर ठरते.",
        "hi": "गन्ने की फसल के लिए, जब चीनी का  'औसत ब्रिक्स' (Avg Brix)  एक निश्चित स्तर से ऊपर (जैसे १९-२०) हो जाता है, तब कटाई का निर्णय लेना फायदेमंद होता है।",
        "en": "For sugarcane, it is profitable to decide on harvesting when the  'Avg Brix'  level goes above a specific threshold (e.g., 19-20)."
    },
    "days_to_harvest_negative": {
        "keywords": ["डेज टू हार्वेस्ट नकारात्मक", "harvest negative", "नकारात्मक संख्या", "कटाई के दिन माइनस", "overdue"],
        "mr": "नकारात्मक संख्या याचा अर्थ  नियोजित कापणीची वेळ निघून गेली आहे  आणि पीक उशिरा काढले जात आहे किंवा शेड्यूलमध्ये बदल करणे आवश्यक आहे.",
        "hi": "नकारात्मक संख्या का अर्थ है कि  योजनाबद्ध कटाई का समय निकल चुका है  और फसल देर से काटी जा रही है या आपको शेड्यूल बदलना होगा।",
        "en": "A negative number means the  planned harvest time is overdue , and the crop is being harvested late, or the schedule needs adjustment."
    },
    "recovery_rate_improve_potash": {
        "keywords": ["रिकव्हरी रेट सुधारण्यासाठी उपाय", "improve recovery rate", "पोटॅश", "potash", "रिकवरी रेट"],
        "mr": "'रिकव्हरी रेट' वाढवण्यासाठी पिकाच्या योग्य टप्प्यावर  पोटॅश (Potash) आणि सल्फर (Sulphur)  सारख्या पोषक तत्वांचा योग्य प्रमाणात वापर करणे महत्त्वाचे आहे.",
        "hi": "'रिकवरी रेट' बढ़ाने के लिए फसल के सही चरण में  पोटाश (Potash) और सल्फर (Sulphur)  जैसे पोषक तत्वों का सही मात्रा में उपयोग करना महत्वपूर्ण है।",
        "en": "To increase the 'Recovery Rate', it is important to use the right amount of nutrients like  Potash and Sulphur  at the appropriate crop stage."
    },
    "yield_projection_accuracy": {
        "keywords": ["यील्ड प्रोजेक्शनची अचूकता", "yield projection accuracy", "उत्पादन अनुमान की सटीकता", "accuracy"],
        "mr": "हे AI मॉडेलची अचूकता (Accuracy)  ९०% किंवा त्याहून अधिक  असते, परंतु हवामानातील मोठे आणि अनपेक्षित बदल या अंदाजावर परिणाम करू शकतात.",
        "hi": "इस AI मॉडल की सटीकता (Accuracy)  ९०% या उससे अधिक  होती है, परंतु मौसम में बड़े और अप्रत्याशित बदलाव इस अनुमान को प्रभावित कर सकते हैं।",
        "en": "The accuracy of this AI model is  90% or higher , but large and unexpected changes in weather can affect this prediction."
    },
    # ----------------------------------------------------------------------
    # ६. डॅशबोर्ड आणि ॲप कार्यक्षमता (Dashboard & App Features)
    # ----------------------------------------------------------------------
    "field_area_measurement": {
        "keywords": ["फील्ड एरिया", "field area", "खेत का क्षेत्रफल", "क्षेत्रफल कैसे मापा", "geo-fencing"],
        "mr": "CropEye.ai तुमच्या शेताच्या GPS आणि उपग्रह प्रतिमा (Satellite Imagery) डेटा वापरून नकाशावर सीमांकन ( Geo-fencing ) करून अचूक मापन करते.",
        "hi": "CropEye.ai आपके खेत के GPS और उपग्रह छवियों का उपयोग करके मानचित्र पर जियो-फेंसिंग करके सटीक मापन करता है।",
        "en": "CropEye.ai performs accurate measurement by using GPS and satellite imagery data to define the boundaries ( Geo-fencing ) of your farm on the map."
    },
    "low_yield_area_map": {
        "keywords": ["उत्पादन कमी येण्याची शक्यता नकाशावर", "low yield area map", "कम उत्पादन वाला क्षेत्र", "zone management"],
        "mr": "होय, CropEye.ai 'झोन मॅनेजमेंट' (Zone Management) नकाशावर  'ग्रोथ इंडेक्स' सर्वात कमी असलेल्या भागांना चिन्हांकित करून दाखवते, जिथे उत्पादन कमी असेल.",
        "hi": "हाँ, CropEye.ai 'ज़ोन मैनेजमेंट' (Zone Management) मानचित्र  पर 'ग्रोथ इंडेक्स' सबसे कम वाले क्षेत्रों को चिह्नित करके दिखाता है, जहाँ उत्पादन कम होगा।",
        "en": "Yes, CropEye.ai shows areas with the lowest 'Growth Index' by marking them on the  'Zone Management' map ."
    },
    "dashboard_alerts_phone": {
        "keywords": ["सूचना फोनवर मेसेजद्वारे", "dashboard alerts phone", "अलर्ट मैसेज", "notifications"],
        "mr": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "hi": "हाँ, CropEye.ai ॲप आपको  'सिंचाई की आवश्यकता'  या  'तनाव का खतरा'  जैसी महत्वपूर्ण सूचनाएं (Alerts) सीधे फोन पर मैसेज या नोटिफिकेशन के माध्यम से भेजने की सुविधा देता है।",
        "en": "Yes, the CropEye.ai app allows you to send important Alerts like  'Irrigation Need'  or  'Stress Risk'  directly to your phone via message or notification."
    },
    "historical_data_comparison": {
        "keywords": ["मागील वर्षाच्या डेटा सोबत तुलना", "historical data comparison", "पिछले साल का डेटा", "comparison"],
        "mr": "डॅशबोर्डवर 'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "hi": "डॅशबोर्ड पर  'इयरली' (Yearly) या 'तुलना' (Comparison)  विकल्प चुनकर आप ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स और उत्पादन अनुमान की तुलना कर सकते हैं।",
        "en": "You can compare the Growth Index, Stress Index, and Yield Projection by selecting the  'Yearly' or 'Comparison'  option on the dashboard."
    },
    "file_report_records": {
        "keywords": ["फाइल रिपोर्ट मध्ये नोंदी", "file report records", "फाइल रिपोर्ट में रिकॉर्ड", "activity logs"],
        "mr": "तुम्ही  खतांचा वापर, फवारणी, सिंचनाच्या वेळा, मजुरीचा खर्च  आणि इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "hi": "आप  खाद का उपयोग, छिड़काव, सिंचाई का समय, मजदूरी का खर्च  और अन्य सभी खेत की गतिविधियों का रिकॉर्ड रख सकते हैं।",
        "en": "You can keep records of  fertilizer usage, spraying, irrigation times, labor costs , and all other farm activities."
    },
    # ----------------------------------------------------------------------
    # ७. इतर प्रगत प्रश्न (Other Advanced Questions)
    # ----------------------------------------------------------------------
    "biomass_yield_projection_relation": {
        "keywords": ["बायोमास उत्पादन अंदाज संबंध", "biomass yield projection relation", "कुल बायोमास", "biomass relation"],
        "mr": "'एकूण बायोमास' हे पिकाच्या वाढीचे वर्तमान वजन आहे, जे 'उत्पादन अंदाजा'साठी आधारभूत आहे.  जास्त बायोमास म्हणजे जास्त उत्पादन  मिळण्याची शक्यता.",
        "hi": "'कुल बायोमास' फसल की वृद्धि का वर्तमान वजन है, जो 'उत्पादन अनुमान' के लिए आधार है।  अधिक बायोमास का अर्थ है अधिक उत्पादन  मिलने की संभावना।",
        "en": "Total Biomass is the current weight of crop growth, which is the basis for the 'Yield Projection'.  More biomass means a higher probability of higher yield ."
    },
    "stress_events_zero": {
        "keywords": ["स्ट्रेस इव्हेंट्स शून्य आहेत", "stress events zero", "तनाव घटनाएं शून्य", "micro-deficiency"],
        "mr": "शून्य 'स्ट्रेस इव्हेंट्स' म्हणजे सध्या कोणतेही मोठे धोके नाहीत. तथापि, 'ग्रोथ इंडेक्स' स्थिर किंवा कमी होत असल्यास,  सूक्ष्म कमतरता (Micro-Deficiency)  असू शकते.",
        "hi": "शून्य 'तनाव घटनाओं' का मतलब है कि वर्तमान में कोई बड़ा खतरा नहीं है। हालांकि, यदि 'ग्रोथ इंडेक्स' स्थिर या कम हो रहा है, तो  सूक्ष्म कमी (Micro-Deficiency)  हो सकती है।",
        "en": "Zero 'Stress Events' means there are no major risks currently. However, if the 'Growth Index' is stable or decreasing, there might be a  Micro-Deficiency ."
    },
    "low_yield_high_recovery": {
        "keywords": ["रिकव्हरी रेट चांगला असूनही उत्पादन कमी", "high recovery low yield", "रिकवरी रेट अच्छा फिर भी", "quality vs quantity"],
        "mr": "'रिकव्हरी रेट' (गुणवत्ता) चांगला असला तरी, तुमचा  'एकूण बायोमास' कमी  असेल, तर एकूण उत्पादन (Total Quantity) कमीच राहील. गुणवत्तेऐवजी आता पिकाच्या वजनावर लक्ष द्या.",
        "hi": "'रिकवरी रेट' (गुणवत्ता) अच्छा होने के बावजूद, यदि आपका  'कुल बायोमास' कम  है, तो कुल उत्पादन (Total Quantity) कम ही रहेगा। गुणवत्ता के बजाय अब फसल के वजन पर ध्यान दें।",
        "en": "Even if the 'Recovery Rate' (quality) is good, if your  'Total Biomass' is low , the total yield (Total Quantity) will remain low. Focus on weight instead of just quality."
    },
    # ----------------------------------------------------------------------
    # ⚠️ फॉलबॅक मेसेज (Fallback Messages)
    # ----------------------------------------------------------------------
    "fallback_message": {
        "keywords": ["fallback_trigger"],
        "mr": "क्षमा करा, API काम करत नाहीये आणि या प्रश्नाचे उत्तर आमच्या QA ज्ञान आधारामध्ये उपलब्ध नाही. कृपया वेगळा प्रश्न विचारा.",
        "hi": "क्षमा करें, API काम नहीं कर रहा है और इस प्रश्न का उत्तर हमारे QA ज्ञान आधार में उपलब्ध नहीं है। कृपया कोई और प्रश्न पूछें।",
        "en": "The API is currently unavailable, and the answer to this specific question is not found in our QA Knowledge Base. Please ask a different question."
    },
    "what_is_cropeye": {
        "keywords": ["what is cropeye", "cropeye काय आहे", "cropeye क्या है", "क्रॉप आय माहिती", "मुख्य काम", "what does cropeye do","cropeye"],
        "mr": "CropEye.ai हे  प्रगत प्रेसिजन शेतीचे (Precision Farming) साधन  आहे, जे  AI आणि उपग्रह (Satellite) तंत्रज्ञान  वापरून पिकाचे आरोग्य, उत्पादन अंदाज आणि पाणी-खत व्यवस्थापनासाठी  अचूक मार्गदर्शन  करते. याचे मुख्य उद्दिष्ट डेटा-आधारित निर्णय घेण्यास मदत करणे आहे.",
        "hi": "CropEye.ai एक  एडवांस्ड प्रिसीजन फार्मिंग समाधान  है जो  AI, सैटेलाइट इमेजरी और डेटा विश्लेषण  का उपयोग करके फसल के स्वास्थ्य, उपज अनुमान, और संसाधन प्रबंधन के लिए  वास्तविक समय की जानकारी  प्रदान करता है।",
        "en": "CropEye.ai is a  comprehensive precision farming solution  that uses  AI and satellite technology  to provide real-time, actionable insights for crop health, yield optimization, and resource management."
    },
    "data_source": {
        "keywords": ["data source", "डेटा कुठून येतो", "माहितीचे स्रोत", "data kahan se aata hai", "source of information"],
        "mr": "माहिती प्रामुख्याने  उपग्रह प्रतिमा (Satellite Imagery) ,  हवामान डेटा (Weather Data) ,  शेतकऱ्यांनी भरलेला ग्राउंड डेटा  आणि  AI ॲनालिसिस मॉडेल  मधून येते.",
        "hi": "जानकारी मुख्य रूप से  उपग्रह छवियों (Satellite Imagery) ,  मौसम डेटा ,  किसानों द्वारा भरे गए ग्राउंड डेटा  और  AI एनालिसिस मॉडल  से आती है।",
        "en": "The data primarily comes from  Satellite Imagery ,  Weather Data ,  Ground Data  fed by farmers, and  AI analysis models ."
    },
    "crop_suitability": {
        "keywords": ["कोणत्या पिकांसाठी योग्य", "which crops are supported", "किसानों फसलें", "ऊस", "sugarcane", "धान्य"],
        "mr": "CropEye.ai हे ऊसासारख्या (Sugarcane)  दीर्घकालीन पिकांसाठी आणि  धान्य, कापूस  यांसारख्या अनेक प्रमुख पिकांसाठी डिझाइन केलेले आहे.",
        "hi": "CropEye.ai  गन्ने (Sugarcane)  जैसी लंबी अवधि की फसलों और  अनाज, कपास  जैसी कई प्रमुख फसलों के लिए डिज़ाइन किया गया है।",
        "en": "CropEye.ai is designed for long-duration crops like  Sugarcane , as well as many major crops like  cereals and cotton ."
    },
    # ----------------------------------------------------------------------
    # २. फील्ड इंडायसेस (Field Indices) आणि पिकाचे आरोग्य
    # ----------------------------------------------------------------------
    "growth_index_low_reason": {
        "keywords": ["ग्रोथ इंडेक्स कमी का", "growth index low reason", "ग्रोथ इंडेक्स कम क्यों"],
        "mr": "'ग्रोथ इंडेक्स' कमी होण्याची मुख्य कारणे म्हणजे  पाण्याची कमतरता , पोषक तत्वांची (उदा. नायट्रोजन) कमतरता किंवा पिकावर आलेला  ताण (Stress) .",
        "hi": "'ग्रोथ इंडेक्स' कम होने के मुख्य कारण  पानी की कमी , पोषक तत्वों की कमी या फसल पर आया हुआ  तनाव (Stress)  हैं।",
        "en": "The main reasons for a low 'Growth Index' are  water deficit , lack of nutrients (e.g., Nitrogen), or  stress  on the crop."
    },
    "growth_index_optimal_level": {
        "keywords": ["ग्रोथ इंडेक्स कोणत्या पातळीवर", "growth index optimal level", "ग्रोथ इंडेक्स स्तर", "योग्य NDVI"],
        "mr": "पिकाच्या प्रकारानुसार आणि टप्प्यानुसार ही पातळी बदलते, परंतु शक्यतो हा निर्देशांक  ०.७५ ते ०.९०  दरम्यान आणि स्थिर राखणे फायदेशीर असते.",
        "hi": "फसल के प्रकार और चरण के अनुसार यह स्तर बदलता है, लेकिन इसे  ०.७५ से ०.९०  के बीच और स्थिर बनाए रखना फायदेमंद होता है।",
        "en": "The optimal Growth Index level usually ranges between  0.75 and 0.90 , depending on the crop and its growth stage."
    },
    "stress_index_high_first_step": {
        "keywords": ["स्ट्रेस इंडेक्स वाढल्यास उपाययोजना", "stress index high first step", "स्ट्रेस इंडेक्स उपाय", "तणाव वाढला"],
        "mr": "'स्ट्रेस इंडेक्स' वाढल्यास प्रथम  मातीतील ओलावा तपासावा . पाण्याची कमतरता असल्यास  त्वरित सिंचन  सुरू करावे; नसेल तर रोगतज्ज्ञांचा सल्ला घ्यावा.",
        "hi": "'स्ट्रेस इंडेक्स' बढ़ने पर, सबसे पहले  मिट्टी की नमी जांचें । पानी की कमी होने पर  तुरंत सिंचाई  शुरू करें; अन्यथा, रोग विशेषज्ञ से सलाह लें।",
        "en": "If the 'Stress Index' is high, first  check the soil moisture . If there's a water deficit,  start irrigation immediately ; otherwise, consult a pathologist."
    },
    "stress_index_disease_detection": {
        "keywords": ["स्ट्रेस इंडेक्स रोग ओळखू शकतो", "stress index disease detection", "रोग पहचान", "disease detection"],
        "mr": "'स्ट्रेस इंडेक्स'  रोगांमुळे आलेला ताण  (उदा. बुरशीजन्य रोग) ओळखू शकतो, परंतु विशिष्ट रोगाचे नाव देण्यासाठी शेतकऱ्यांनी ग्राउंड व्हिजिट करणे आवश्यक आहे.",
        "hi": "'स्ट्रेस इंडेक्स'  रोगों के कारण हुए तनाव  (जैसे फंगल रोग) को पहचान सकता है, लेकिन विशिष्ट रोग का नाम बताने के लिए किसानों को ग्राउंड विज़िट करना आवश्यक है।",
        "en": "The 'Stress Index' can identify  stress caused by diseases  (e.g., fungal diseases), but farmers need to conduct a ground visit to name the specific disease."
    },
    "growth_index_low_fertilizer": {
        "keywords": ["ग्रोथ इंडेक्स सुधारणा खत", "growth index fertilizer", "ग्रोथ इंडेक्स खाद", "युरिया", "नाइट्रोजन"],
        "mr": "ग्रोथ इंडेक्स थेट  नायट्रोजनच्या कमतरतेशी  संबंधित असतो. त्यामुळे नायट्रोजनयुक्त खत (उदा. युरिया) त्वरित देण्याची शिफारस केली जाते.",
        "hi": "ग्रोथ इंडेक्स सीधे  नाइट्रोजन की कमी  से संबंधित होता है। इसलिए, नाइट्रोजन युक्त खाद (जैसे यूरिया) तुरंत देने की सिफारिश की जाती है।",
        "en": "The Growth Index is directly linked to  Nitrogen deficiency . Immediate application of Nitrogen-rich fertilizer (e.g., Urea) is recommended."
    },
    # ----------------------------------------------------------------------
    # ३. जल व्यवस्थापन (Water Management)
    # ----------------------------------------------------------------------
    "water_vs_moisture_index": {
        "keywords": ["वॉटर इंडेक्स मॉईश्चर इंडेक्स फरक", "water moisture index difference", "पानी और नमी सूचकांक", "पानांमधील पाणी"],
        "mr": " 'वॉटर इंडेक्स'  पिकाच्या  पानांमधील पाण्याची मात्रा  दर्शवतो, तर  'मॉईश्चर इंडेक्स'   मातीतील ओलाव्याचे प्रमाण  दर्शवतो.",
        "hi": " 'वॉटर इंडेक्स'  फसल की  पत्तियों में पानी की मात्रा  दर्शाता है, जबकि  'मॉइश्चर इंडेक्स'   मिट्टी की नमी की मात्रा  दर्शाता है।",
        "en": "The  'Water Index'  shows the  amount of water in the crop leaves , while the  'Moisture Index'  shows the  amount of moisture in the soil ."
    },
    "moisture_index_irrigation_level": {
        "keywords": ["मॉईश्चर इंडेक्स सिंचन पातळी", "moisture index irrigation level", "नमी सूचकांक सिंचाई", "किती झाल्यावर पाणी द्यावे"],
        "mr": "जेव्हा 'मॉईश्चर इंडेक्स'  ५०% च्या खाली  जातो, तेव्हा  त्वरित सिंचनाची  शिफारस केली जाते.",
        "hi": "जब 'मॉइश्चर इंडेक्स'  ५०% से नीचे  चला जाता है, तब  तुरंत सिंचाई  करने की सिफारिश की जाती है।",
        "en": "When the 'Moisture Index' drops  below 50% ,  immediate irrigation  is recommended."
    },
    "irrigation_schedule_change": {
        "keywords": ["सिंचन वेळापत्रक आपोआप बदलते", "irrigation schedule auto change", "सिंचाई का समय", "schedule badalta hai"],
        "mr": "होय, CropEye.ai चे 'इरिगेशन शेड्यूल' पिकाच्या टप्प्यांमध्ये पाण्याच्या गरजेनुसार आणि  हवामान बदलांनुसार  आपोआप बदलले जाते.",
        "hi": "हाँ, CropEye.ai का 'सिंचाई शेड्यूल' फसल के चरणों में पानी की आवश्यकता और  मौसम के बदलावों के अनुसार  स्वचालित रूप से बदल जाता है।",
        "en": "Yes, CropEye.ai's 'Irrigation Schedule' is automatically adjusted according to the water needs during the crop stages and  weather changes ."
    },
    "water_index_no_improvement": {
        "keywords": ["सिंचन केल्यावरही वॉटर इंडेक्स सुधारत नाही", "water index no improvement", "सिंचाई के बाद भी सुधार नहीं"],
        "mr": "याचा अर्थ मुळांना पाणी शोषण्यात अडचण येत आहे. हे कदाचित  माती घट्ट झाल्यामुळे (Compaction)  किंवा मुळांना रोग झाल्यामुळे असू शकते.",
        "hi": "इसका मतलब है कि जड़ों को पानी सोखने में दिक्कत आ रही है। यह शायद  मिट्टी के सख्त होने (Compaction)  या जड़ों में रोग होने के कारण हो सकता है।",
        "en": "This means the roots are having trouble absorbing water. This may be due to  soil compaction  or root diseases."
    },
    "weather_forecast_irrigation_planning": {
        "keywords": ["७ दिवसांच्या हवामान अंदाजानुसार सिंचन नियोजन", "weather forecast irrigation planning", "मौसम अनुमान सिंचाई", "पावसाचा अंदाज"],
        "mr": "जर पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "hi": "यदि अगले ४८ घंटों में भारी बारिश का अनुमान है, तो  सिंचाई रोक दें । यदि तापमान बढ़ने वाला है, तो सिंचाई की मात्रा बढ़ा दें।",
        "en": "If heavy rain is forecast in the next 48 hours,  stop irrigation . If the temperature is going to rise, increase the amount of irrigation."
    },
    # ----------------------------------------------------------------------
    # ४. माती आणि पोषण व्यवस्थापन (Soil & Nutrition Management)
    # ----------------------------------------------------------------------
    "organic_carbon_optimal": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी किती", "organic carbon optimal level", "सेंद्रिय कर्ब", "organic carbon density"],
        "mr": "साधारणपणे, सेंद्रिय कर्बाचे प्रमाण  ०.५% पेक्षा जास्त  (म्हणजेच gm/cm³ मध्ये जास्त) असल्यास मातीची गुणवत्ता चांगली मानली जाते.",
        "hi": "सामान्यतः, यदि कार्बनिक कार्बन की मात्रा  ०.५% से अधिक  है तो मिट्टी की गुणवत्ता अच्छी मानी जाती है।",
        "en": "Generally, soil quality is considered good if the organic carbon content is  greater than 0.5% ."
    },
    "organic_carbon_improve": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी सुधारण्यासाठी खत", "improve organic carbon", "सेंद्रिय खत", "कंपोस्ट"],
        "mr": " शेणखत, कंपोस्ट खत, गांडूळ खत  किंवा हिरवळीची खते (Green Manure) वापरून 'ऑरगॅनिक कार्बन डेन्सिटी' सुधारता येते.",
        "hi": " गोबर की खाद, कंपोस्ट खाद, केंचुआ खाद  या हरी खाद (Green Manure) का उपयोग करके 'कार्बनिक कार्बन घनत्व' में सुधार किया जा सकता है।",
        "en": " Cow dung manure, compost, vermicompost,  or green manures can be used to improve 'Organic Carbon Density'."
    },
    "soil_ph_sugarcane_optimal": {
        "keywords": ["pH लेव्हल ऊस पिकासाठी योग्य आहे", "soil ph level sugarcane", "pH 7.30", "मातीचा पीएच"],
        "mr": " ७.३० pH  ऊस पिकासाठी स्वीकार्य आहे (ऊस ६.० ते ८.५ pH मध्ये वाढतो). pH जास्त असल्यास  गंधक (Sulphur)  वापरावा आणि कमी असल्यास  चुना (Lime)  वापरावा.",
        "hi": " ७.३० pH  गन्ने की फसल के लिए स्वीकार्य है। pH अधिक होने पर  सल्फर (Sulphur)  का उपयोग करें और कम होने पर  चूना (Lime)  का उपयोग करें।",
        "en": " 7.30 pH  is acceptable for sugarcane. Use  Sulphur  if the pH is high and  Lime  if it is low."
    },
    "fertilizer_recommendation": {
        "keywords": ["कोणत्या विशिष्ट खतांची गरज", "fertilizer recommendation NPK", "खाद की सिफारिश", "NPK", "सूक्ष्म पोषक तत्व"],
        "mr": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "hi": "हाँ, 'ग्रोथ इंडेक्स' और मिट्टी pH स्तर का विश्लेषण करके डॅशबोर्ड  NPK और सूक्ष्म पोषक तत्वों (Micro-Nutrients)  की सिफारिश करता है।",
        "en": "Yes, by analyzing the 'Growth Index' and soil pH level, the dashboard recommends  NPK and Micro-Nutrients ."
    },
    "soil_ph_nutrient_relation": {
        "keywords": ["pH पोषक तत्वांची उपलब्धता", "ph nutrient relation", "pH और पोषक तत्व", "nutrient availability"],
        "mr": "मातीचा pH योग्य असल्यास (उदा. ६.५ ते ७.५),  नायट्रोजन, फॉस्फरस आणि पोटॅशसह बहुतेक पोषक तत्त्वे  पिकांसाठी सहज उपलब्ध होतात. pH बदलल्यास उपलब्धता कमी होते.",
        "hi": "यदि मिट्टी का pH सही है (जैसे ६.५ से ७.५), तो  नाइट्रोजन, फास्फोरस और पोटाश सहित अधिकांश पोषक तत्व  फसलों के लिए आसानी से उपलब्ध होते हैं।",
        "en": "If the soil pH is correct (e.g., 6.5 to 7.5),  most nutrients, including NPK , are readily available to crops. Availability decreases if the pH changes."
    },
    # ----------------------------------------------------------------------
    # ५. उत्पादन आणि कापणी (Yield & Harvest Management)
    # ----------------------------------------------------------------------
    "projected_vs_optimal_yield": {
        "keywords": ["प्रोजेक्टेड यील्ड कमी का", "projected vs optimal yield", "उत्पादन अंदाज कम क्यों", "optimal yield"],
        "mr": "'प्रोजेक्टेड यील्ड' तुमच्या सध्याच्या व्यवस्थापनावर आधारित आहे, तर 'ऑप्टिमल यील्ड' हे  सर्वात चांगल्या परिस्थितीत  शक्य असलेले उत्पादन आहे. व्यवस्थापन सुधारून तुम्ही ऑप्टिमल यील्ड गाठू शकता.",
        "hi": "'प्रोजेक्टेड यील्ड' आपके वर्तमान प्रबंधन पर आधारित है, जबकि 'ऑप्टिमल यील्ड'  सर्वोत्तम परिस्थितियों  में संभव उत्पादन है। प्रबंधन में सुधार करके आप ऑप्टिमल यील्ड तक पहुँच सकते हैं।",
        "en": "'Projected Yield' is based on your current management, while 'Optimal Yield' is the production possible under  the best possible conditions . You can reach optimal yield by improving management."
    },
    "sugar_content_harvest": {
        "keywords": ["साखर कंटेंट कापणी", "sugar content harvest", "शुगर कंटेंट", "रिकव्हरी मिळेल", "brix"],
        "mr": "ऊस पिकासाठी, साखरेचा  'सरासरी ब्रिक्स' (Avg Brix)  जेव्हा विशिष्ट पातळीपेक्षा जास्त (उदा. १९-२०) होतो, तेव्हा कापणीसाठी तोडगा काढणे फायदेशीर ठरते.",
        "hi": "गन्ने की फसल के लिए, जब चीनी का  'औसत ब्रिक्स' (Avg Brix)  एक निश्चित स्तर से ऊपर (जैसे १९-२०) हो जाता है, तब कटाई का निर्णय लेना फायदेमंद होता है।",
        "en": "For sugarcane, it is profitable to decide on harvesting when the  'Avg Brix'  level goes above a specific threshold (e.g., 19-20)."
    },
    "days_to_harvest_negative": {
        "keywords": ["डेज टू हार्वेस्ट नकारात्मक", "harvest negative", "नकारात्मक संख्या", "कटाई के दिन माइनस", "overdue"],
        "mr": "नकारात्मक संख्या याचा अर्थ  नियोजित कापणीची वेळ निघून गेली आहे  आणि पीक उशिरा काढले जात आहे किंवा शेड्यूलमध्ये बदल करणे आवश्यक आहे.",
        "hi": "नकारात्मक संख्या का अर्थ है कि  योजनाबद्ध कटाई का समय निकल चुका है  और फसल देर से काटी जा रही है या आपको शेड्यूल बदलना होगा।",
        "en": "A negative number means the  planned harvest time is overdue , and the crop is being harvested late, or the schedule needs adjustment."
    },
    "recovery_rate_improve_potash": {
        "keywords": ["रिकव्हरी रेट सुधारण्यासाठी उपाय", "improve recovery rate", "पोटॅश", "potash", "रिकवरी रेट"],
        "mr": "'रिकव्हरी रेट' वाढवण्यासाठी पिकाच्या योग्य टप्प्यावर  पोटॅश (Potash) आणि सल्फर (Sulphur)  सारख्या पोषक तत्वांचा योग्य प्रमाणात वापर करणे महत्त्वाचे आहे.",
        "hi": "'रिकवरी रेट' बढ़ाने के लिए फसल के सही चरण में  पोटाश (Potash) और सल्फर (Sulphur)  जैसे पोषक तत्वों का सही मात्रा में उपयोग करना महत्वपूर्ण है।",
        "en": "To increase the 'Recovery Rate', it is important to use the right amount of nutrients like  Potash and Sulphur  at the appropriate crop stage."
    },
    "yield_projection_accuracy": {
        "keywords": ["यील्ड प्रोजेक्शनची अचूकता", "yield projection accuracy", "उत्पादन अनुमान की सटीकता", "accuracy"],
        "mr": "हे AI मॉडेलची अचूकता (Accuracy)  ९०% किंवा त्याहून अधिक  असते, परंतु हवामानातील मोठे आणि अनपेक्षित बदल या अंदाजावर परिणाम करू शकतात.",
        "hi": "इस AI मॉडल की सटीकता (Accuracy)  ९०% या उससे अधिक  होती है, परंतु मौसम में बड़े और अप्रत्याशित बदलाव इस अनुमान को प्रभावित कर सकते हैं।",
        "en": "The accuracy of this AI model is  90% or higher , but large and unexpected changes in weather can affect this prediction."
    },
    # ----------------------------------------------------------------------
    # ६. डॅशबोर्ड आणि ॲप कार्यक्षमता (Dashboard & App Features)
    # ----------------------------------------------------------------------
    "field_area_measurement": {
        "keywords": ["फील्ड एरिया", "field area", "खेत का क्षेत्रफल", "क्षेत्रफल कैसे मापा", "geo-fencing"],
        "mr": "CropEye.ai तुमच्या शेताच्या GPS आणि उपग्रह प्रतिमा (Satellite Imagery) डेटा वापरून नकाशावर सीमांकन ( Geo-fencing ) करून अचूक मापन करते.",
        "hi": "CropEye.ai आपके खेत के GPS और उपग्रह छवियों का उपयोग करके मानचित्र पर जियो-फेंसिंग करके सटीक मापन करता है।",
        "en": "CropEye.ai performs accurate measurement by using GPS and satellite imagery data to define the boundaries ( Geo-fencing ) of your farm on the map."
    },
    "low_yield_area_map": {
        "keywords": ["उत्पादन कमी येण्याची शक्यता नकाशावर", "low yield area map", "कम उत्पादन वाला क्षेत्र", "zone management"],
        "mr": "होय, CropEye.ai  'झोन मॅनेजमेंट' (Zone Management) नकाशावर  'ग्रोथ इंडेक्स' सर्वात कमी असलेल्या भागांना चिन्हांकित करून दाखवते, जिथे उत्पादन कमी असेल.",
        "hi": "हाँ, CropEye.ai  'ज़ोन मैनेजमेंट' (Zone Management) मानचित्र  पर 'ग्रोथ इंडेक्स' सबसे कम वाले क्षेत्रों को चिह्नित करके दिखाता है, जहाँ उत्पादन कम होगा।",
        "en": "Yes, CropEye.ai shows areas with the lowest 'Growth Index' by marking them on the  'Zone Management' map ."
    },
    "dashboard_alerts_phone": {
        "keywords": ["सूचना फोनवर मेसेजद्वारे", "dashboard alerts phone", "अलर्ट मैसेज", "notifications"],
        "mr": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "hi": "हाँ, CropEye.ai ॲप आपको  'सिंचाई की आवश्यकता'  या  'तनाव का खतरा'  जैसी महत्वपूर्ण सूचनाएं (Alerts) सीधे फोन पर मैसेज या नोटिफिकेशन के माध्यम से भेजने की सुविधा देता है।",
        "en": "Yes, the CropEye.ai app allows you to send important Alerts like  'Irrigation Need'  or  'Stress Risk'  directly to your phone via message or notification."
    },
    "historical_data_comparison": {
        "keywords": ["मागील वर्षाच्या डेटा सोबत तुलना", "historical data comparison", "पिछले साल का डेटा", "comparison"],
        "mr": "डॅशबोर्डवर  'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "hi": "डॅशबोर्ड पर  'इयरली' (Yearly) या 'तुलना' (Comparison)  विकल्प चुनकर आप ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स और उत्पादन अनुमान की तुलना कर सकते हैं।",
        "en": "You can compare the Growth Index, Stress Index, and Yield Projection by selecting the  'Yearly' or 'Comparison'  option on the dashboard."
    },
    "file_report_records": {
        "keywords": ["फाइल रिपोर्ट मध्ये नोंदी", "file report records", "फाइल रिपोर्ट में रिकॉर्ड", "activity logs"],
        "mr": "तुम्ही  खतांचा वापर, फवारणी, सिंचनाच्या वेळा, मजुरीचा खर्च  आणि इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "hi": "आप  खाद का उपयोग, छिड़काव, सिंचाई का समय, मजदूरी का खर्च  और अन्य सभी खेत की गतिविधियों का रिकॉर्ड रख सकते हैं।",
        "en": "You can keep records of  fertilizer usage, spraying, irrigation times, labor costs , and all other farm activities."
    },
    # ----------------------------------------------------------------------
    # ७. इतर प्रगत प्रश्न (Other Advanced Questions)
    # ----------------------------------------------------------------------
    "biomass_yield_projection_relation": {
        "keywords": ["बायोमास उत्पादन अंदाज संबंध", "biomass yield projection relation", "कुल बायोमास", "biomass relation"],
        "mr": "'एकूण बायोमास' हे पिकाच्या वाढीचे वर्तमान वजन आहे, जे 'उत्पादन अंदाजा'साठी आधारभूत आहे.  जास्त बायोमास म्हणजे जास्त उत्पादन  मिळण्याची शक्यता.",
        "hi": "'कुल बायोमास' फसल की वृद्धि का वर्तमान वजन है, जो 'उत्पादन अनुमान' के लिए आधार है।  अधिक बायोमास का अर्थ है अधिक उत्पादन  मिलने की संभावना।",
        "en": "Total Biomass is the current weight of crop growth, which is the basis for the 'Yield Projection'.  More biomass means a higher probability of higher yield ."
    },
    "stress_events_zero": {
        "keywords": ["स्ट्रेस इव्हेंट्स शून्य आहेत", "stress events zero", "तनाव घटनाएं शून्य", "micro-deficiency"],
        "mr": "शून्य 'स्ट्रेस इव्हेंट्स' म्हणजे सध्या कोणतेही मोठे धोके नाहीत. तथापि, 'ग्रोथ इंडेक्स' स्थिर किंवा कमी होत असल्यास,  सूक्ष्म कमतरता (Micro-Deficiency)  असू शकते.",
        "hi": "शून्य 'तनाव घटनाओं' का मतलब है कि वर्तमान में कोई बड़ा खतरा नहीं है। हालांकि, यदि 'ग्रोथ इंडेक्स' स्थिर या कम हो रहा है, तो  सूक्ष्म कमी (Micro-Deficiency)  हो सकती है।",
        "en": "Zero 'Stress Events' means there are no major risks currently. However, if the 'Growth Index' is stable or decreasing, there might be a  Micro-Deficiency ."
    },
    "low_yield_high_recovery": {
        "keywords": ["रिकव्हरी रेट चांगला असूनही उत्पादन कमी", "high recovery low yield", "रिकवरी रेट अच्छा फिर भी", "quality vs quantity"],
        "mr": "'रिकव्हरी रेट' (गुणवत्ता) चांगला असला तरी, तुमचा  'एकूण बायोमास' कमी  असेल, तर एकूण उत्पादन (Total Quantity) कमीच राहील. गुणवत्तेऐवजी आता पिकाच्या वजनावर लक्ष द्या.",
        "hi": "'रिकवरी रेट' (गुणवत्ता) अच्छा होने के बावजूद, यदि आपका  'कुल बायोमास' कम  है, तो कुल उत्पादन (Total Quantity) कम ही रहेगा। गुणवत्ता के बजाय अब फसल के वजन पर ध्यान दें।",
        "en": "Even if the 'Recovery Rate' (quality) is good, if your  'Total Biomass' is low , the total yield (Total Quantity) will remain low. Focus on weight instead of just quality."
    },
    "low_yield_high_recovery": {
        "keywords": [
        "रिकव्हरी रेट चांगला असूनही उत्पादन कमी",
        "high recovery low yield",
        "रिकवरी रेट अच्छा फिर भी",
        "quality vs quantity",
        "गुणवत्ता विरुद्ध प्रमाण",
        "कमी उत्पादन कारण",
        "biomass importance"
        ],
        "mr": "'रिकव्हरी रेट' (गुणवत्ता) चांगला असला तरी, तुमचा  'एकूण बायोमास' कमी  असेल, तर एकूण उत्पादन (Total Quantity) कमीच राहील. Cropeye.ai च्या  वनस्पती घनता नकाशा (Plant Density Map)  मध्ये पहा की तुमच्या प्लॉटवर झाडांची संख्या/घनता पुरेशी आहे की नाही. गुणवत्तेऐवजी आता पिकाच्या वजनावर लक्ष द्या.",
        "hi": "'रिकवरी रेट' (गुणवत्ता) अच्छा होने के बावजूद, यदि आपका  'कुल बायोमास' कम  है, तो कुल उत्पादन (Total Quantity) कम ही रहेगा। Cropeye.ai के  वनस्पति घनत्व मानचित्र (Plant Density Map)  में देखें कि आपके प्लॉट पर पौधों की संख्या/घनत्व पर्याप्त है या नहीं। गुणवत्ता के बजाय अब फसल के वजन पर ध्यान दें।",
        "en": "Even if the 'Recovery Rate' (quality) is good, if your  'Total Biomass' is low , the total yield (Total Quantity) will remain low. Check your Cropeye.ai  Plant Density Map  to ensure adequate plant count/density on your plot. Focus on weight/volume instead of just quality now."
    },
    "what_is_cropeye": {
        "keywords": [
        "cropeye काय आहे",
        "planeteyefarm ai काय करते",
        "precison farming solution",
        "क्रॉप आय माहिती"
        ],
        "mr": "Cropeye.ai हे PlanetEye Farm-AI द्वारे विकसित केलेले  सेटेलाईट-आधारित ॲप  आहे, जे शेतकऱ्याला पिकाच्या आरोग्याची, पाण्याची गरज आणि खतांची अचूक माहिती देते, ज्यामुळे उत्पादन वाढण्यास मदत होते.",
        "hi": "Cropeye.ai, PlanetEye Farm-AI द्वारा विकसित एक  सेटेलाइट-आधारित ॲप  है, जो किसानों को फसल के स्वास्थ्य, पानी की आवश्यकता और खाद की सटीक जानकारी देता है, जिससे उत्पादन बढ़ाने में मदद मिलती है।",
        "en": "Cropeye.ai is a  satellite-based app  developed by PlanetEye Farm-AI that provides farmers with accurate information on crop health, water needs, and fertilizer requirements to help increase yield."
    },
    "check_crop_health": {
        "keywords": [
        "पिकाचे आरोग्य कसे तपासायचे",
        "NDVI म्हणजे काय",
        "crop stress",
        "तणाव कमी करणे",
        "फसल स्वास्थ्य"
        ],
        "mr": "Cropeye.ai मध्ये 'NDVI' (वनस्पती आरोग्य निर्देशांक) नकाशा तपासा. हिरवा रंग उत्तम आरोग्य, तर लाल किंवा पिवळा रंग  पिकावरील ताण  (उदा. पाण्याची/खतांची कमतरता) दर्शवतो. ताणाचे कारण ओळखून तातडीने उपाययोजना करा.",
        "hi": "Cropeye.ai में 'NDVI' (वनस्पति स्वास्थ्य सूचकांक) मैप जांचें। हरा रंग बेहतरीन स्वास्थ्य दिखाता है, जबकि लाल या पीला रंग  फसल पर तनाव  (जैसे पानी/खाद की कमी) दर्शाता है। तनाव का कारण पहचानें और तुरंत कार्रवाई करें।",
        "en": "Check the 'NDVI' (Vegetation Health Index) map in Cropeye.ai. Green indicates excellent health, while red or yellow indicates  crop stress  (e.g., lack of water/nutrients). Identify the cause of stress and take immediate action."
    },
    "water_management": {
        "keywords": [
        "पाणी व्यवस्थापन",
        "सिंचन कधी करावे",
        "irrigation schedule",
        "पाणी कमी जास्त",
        "water stress map",
        "water"
        ],
        "mr": "Cropeye.ai चा  पाणी ताण नकाशा (Water Stress Map)  तुम्हाला दर्शवेल की पिकाला सिंचनाची कधी गरज आहे. पाण्याचा योग्य वापर करण्यासाठी 'EVAPO' (बाष्पीभवन) डेटा वापरा, जेणेकरून पाण्याची बचत होईल.",
        "hi": "Cropeye.ai का  जल तनाव मानचित्र (Water Stress Map)  आपको दिखाएगा कि फसल को सिंचाई की कब आवश्यकता है। पानी के सही उपयोग के लिए 'EVAPO' (वाष्पीकरण) डेटा का उपयोग करें, जिससे पानी की बचत होगी।",
        "en": "Cropeye.ai's  Water Stress Map  shows you exactly when the crop needs irrigation. Use the 'EVAPO' (Evapotranspiration) data to optimize water usage and conserve water."
    },
    "pest_alert": {
        "keywords": [
        "कीड आणि रोग",
        "रोग निदान",
        "कीटक व्यवस्थापन",
        "pest disease alert",
        "रोगग्रस्त भाग","pest","कीड","रोग"
        ],
        "mr": "Cropeye.ai चा  जोखमीचा नकाशा (Risk Map)  नियमित तपासा. जेव्हा AI पिकाच्या पॅटर्नमध्ये मोठे बदल पाहतो, तेव्हा तो 'कीड/रोग' वाढण्याची शक्यता दर्शवतो. त्या भागात जाऊन तपासणी करा आणि नियंत्रण करा.",
        "hi": "Cropeye.ai का  जोखिम मानचित्र (Risk Map)  नियमित रूप से जांचें। जब AI फसल के पैटर्न में बड़े बदलाव देखता है, तो यह 'कीट/रोग' के बढ़ने की संभावना दर्शाता है। उस क्षेत्र में जाकर निरीक्षण करें और नियंत्रण करें।",
        "en": "Regularly check the Cropeye.ai  Risk Map . When the AI detects significant changes in crop patterns, it signals a potential 'Pest/Disease' outbreak. Go inspect the area and take control measures."
    },
        "company_details": {
        "keywords": [
        "planeteyefarm ai कोणत्या कंपनीची आहे",
        "संस्थापक कोण आहेत",
        "joint venture company",
        "मितकॉन आणि कोलागेन"
        ],
        "mr": "Cropeye.ai विकसित करणारी  PlanetEye Farm-AI Limited  ही MITCON Nature Based Solutions Limited आणि Colagen Research Private Limited ची संयुक्त भागीदारी (Joint Venture) असलेली कंपनी आहे.",
        "hi": "Cropeye.ai विकसित करने वाली  PlanetEye Farm-AI Limited  कंपनी MITCON Nature Based Solutions Limited और Colagen Research Private Limited की एक संयुक्त भागीदारी (Joint Venture) है।",
        "en": " PlanetEye Farm-AI Limited , the company that developed Cropeye.ai, is a Joint Venture between MITCON Nature Based Solutions Limited and Colagen Research Private Limited."
    },
    "contact_email": {
        "keywords": [
        "संपर्क ईमेल",
        "PlanetEye Farm-AI संपर्क",
        "customer support email",
        "ईमेल आयडी"
        ],
        "mr": "PlanetEye Farm-AI शी संपर्क साधण्यासाठी, तुम्ही त्यांच्या अधिकृत कंपनी ईमेल पत्त्यावर (Email ID) संपर्क करू शकता:  cs@mitconindia.com ",
        "hi": "PlanetEye Farm-AI से संपर्क करने के लिए, आप उनके आधिकारिक कंपनी ईमेल पते (Email ID) पर संपर्क कर सकते हैं:  cs@mitconindia.com ",
        "en": "To contact PlanetEye Farm-AI, you can reach out to their official company email address:  cs@mitconindia.com "
    },
    "registered_address": {
        "keywords": [
        "कार्यालय पत्ता",
        "PlanetEye Farm-AI ऑफिस",
        "नोंदणीकृत पत्ता",
        "Pune address"
        ],
        "mr": "PlanetEye Farm-AI Limited चा नोंदणीकृत पत्ता पुणे, महाराष्ट्र येथे आहे:  1st Floor, Kubera Chambers, Shivajinagar, Pune, Maharashtra, India, 411005. ",
        "hi": "PlanetEye Farm-AI Limited का पंजीकृत पता पुणे, महाराष्ट्र में है:  1st Floor, Kubera Chambers, Shivajinagar, Pune, Maharashtra, India, 411005. ",
        "en": "The registered office address for PlanetEye Farm-AI Limited is in Pune, Maharashtra:  1st Floor, Kubera Chambers, Shivajinagar, Pune, Maharashtra, India, 411005. "
    },
    "what_is_cropeye": {
        "keywords": ["what is cropeye", "cropeye काय आहे", "cropeye क्या है", "क्रॉप आय माहिती"],
        "mr": "CropEye.ai हे  प्रगत प्रेसिजन शेतीचे (Precision Farming) साधन  आहे. हे  AI आणि उपग्रह (Satellite) तंत्रज्ञान  वापरून तुमच्या शेतातील पिकांचे आरोग्य, उत्पादन अंदाज आणि पाणी-खत व्यवस्थापनासाठी  अचूक आणि तत्काळ मार्गदर्शन  करते. याचे मुख्य उद्दिष्ट तुम्हाला  डेटा-आधारित निर्णय  घेण्यास मदत करणे आहे.",
        "hi": "CropEye.ai एक  एडवांस्ड प्रिसीजन फार्मिंग समाधान  है जो  AI, सैटेलाइट इमेजरी और डेटा विश्लेषण  का उपयोग करके आपके खेत में फसल के स्वास्थ्य, उपज अनुमान, और संसाधन प्रबंधन (पानी, खाद) के लिए  वास्तविक समय की, कार्रवाई योग्य जानकारी  प्रदान करता है।",
        "en": "CropEye.ai is a  comprehensive precision farming solution  that uses  AI, satellite imagery, and data analysis  to provide real-time, actionable insights for crop health, yield optimization, and resource management (water, fertilizer) on your farm. Its main goal is to help you make  data-driven decisions ."
    },
    "field_area_measurement": {
        "keywords": ["फील्ड एरिया", "field area", "खेत का क्षेत्रफल", "क्षेत्रफल कैसे मापा"],
        "mr": "CropEye.ai तुमच्या शेताच्या GPS आणि उपग्रह प्रतिमा (Satellite Imagery) डेटा वापरून नकाशावर सीमांकन (Geo-fencing) करून अचूक मापन करते.",
        "hi": "CropEye.ai आपके खेत के GPS और उपग्रह छवियों (Satellite Imagery) का उपयोग करके मानचित्र पर जियो-फेंसिंग करके सटीक मापन करता है।",
        "en": "CropEye.ai performs accurate measurement by using GPS and satellite imagery data to define the boundaries (Geo-fencing) of your farm on the map."
    },
    "crop_status_change": {
        "keywords": ["क्रॉप स्टेटस", "पीक स्थिती", "crop status", "फसल की स्थिति"],
        "mr": "हा बदल पिकाच्या वाढीच्या टप्प्यावर आधारित असतो. हे AI मॉडेल पिकाच्या वाढीचे विश्लेषण करून आणि तुम्ही पेरणीची तारीख नोंदवल्यावर निश्चित होते.",
        "hi": "यह परिवर्तन फसल के विकास चरण पर आधारित होता है। यह AI मॉडल फसल की वृद्धि का विश्लेषण करके और आपके बुवाई की तारीख दर्ज करने पर निर्धारित होता है।",
        "en": "This change is based on the crop's growth stage. It is determined by the AI model analyzing crop growth and the planting date you entered."
    },
    "days_to_harvest_negative": {
        "keywords": ["डेज टू हार्वेस्ट नकारात्मक", "harvest negative", "नकारात्मक संख्या", "कटाई के दिन माइनस"],
        "mr": "नकारात्मक संख्या याचा अर्थ  नियोजित कापणीची वेळ निघून गेली आहे  आणि पीक उशिरा काढले जात आहे किंवा शेड्यूलमध्ये बदल करणे आवश्यक आहे.",
        "hi": "नकारात्मक संख्या का अर्थ है कि  योजनाबद्ध कटाई का समय निकल चुका है  और फसल देर से काटी जा रही है या आपको शेड्यूल बदलना होगा।",
        "en": "A negative number means the  planned harvest time is overdue , and the crop is being harvested late, or the schedule needs adjustment."
    },
    "sugar_content_harvest": {
        "keywords": ["साखर कंटेंट कापणी", "sugar content harvest", "शुगर कंटेंट", "रिकव्हरी मिळेल"],
        "mr": "ऊस पिकासाठी, साखरेचा  'सरासरी ब्रिक्स' (Avg Brix)  जेव्हा विशिष्ट पातळीपेक्षा जास्त (उदा. १९-२०) होतो, तेव्हा कापणीसाठी तोडगा काढणे फायदेशीर ठरते.",
        "hi": "गन्ने की फसल के लिए, जब चीनी का  'औसत ब्रिक्स' (Avg Brix)  एक निश्चित स्तर से ऊपर (जैसे १९-२०) हो जाता है, तब कटाई का निर्णय लेना फायदेमंद होता है।",
        "en": "For sugarcane, it is profitable to decide on harvesting when the  'Avg Brix'  level goes above a specific threshold (e.g., 19-20)."
    },
    "sugar_content_max_min": {
        "keywords": ["मॅक्स मिन शुगर कंटेंट", "max min sugar", "कमाल किमान साखर"],
        "mr": "ही मूल्ये शेताच्या विविध विभागातून (उदा. नमुना घेऊन) घेतलेल्या मापनांवर आधारित असतात, जेणेकरून शेतातील  साखरेच्या गुणवत्तेतील तफावत  कळेल.",
        "hi": "ये मान खेत के विभिन्न हिस्सों (जैसे नमूना लेकर) से लिए गए मापों पर आधारित होते हैं, ताकि खेत में  चीनी की गुणवत्ता में अंतर  पता चले।",
        "en": "These values are based on measurements taken from various sections of the field (e.g., by sampling) to show  variation in sugar quality  across the farm."
    },
    "irrigation_schedule_change": {
        "keywords": ["सिंचन वेळापत्रक आपोआप बदलते", "irrigation schedule auto change", "सिंचाई का समय"],
        "mr": "होय, CropEye.ai चे 'इरिगेशन शेड्यूल' (Irrigation Schedule) पिकाच्या टप्प्यांमध्ये पाण्याच्या गरजेनुसार  आपोआप बदलले जाते .",
        "hi": "हाँ, CropEye.ai का 'सिंचाई शेड्यूल' (Irrigation Schedule) फसल के चरणों में पानी की आवश्यकता के अनुसार  स्वचालित रूप से बदल जाता है ।",
        "en": "Yes, CropEye.ai's 'Irrigation Schedule' is  automatically adjusted  according to the water needs during the crop stages."
    },
    "field_area_difference": {
        "keywords": ["एरिया वेगळा का आहे", "field area difference", "क्षेत्रफल अलग क्यों है"],
        "mr": "तुमचा नोंदणीकृत एरिया तुमच्या GPS नोंदीवर आधारित आहे. शेजारच्या शेताचा एरिया त्यांच्या नोंदी आणि उपग्रह नकाशावर काढलेल्या त्यांच्या हद्दीनुसार निश्चित होतो.",
        "hi": "आपका पंजीकृत क्षेत्रफल आपके GPS रिकॉर्ड पर आधारित है। पड़ोसी खेत का क्षेत्रफल उनके रिकॉर्ड और उपग्रह मानचित्र पर खींची गई उनकी सीमाओं के अनुसार निर्धारित होता है।",
        "en": "Your registered area is based on your GPS records. The neighbor's area is determined by their records and the boundaries drawn on the satellite map."
    },
    "harvest_days_yield_impact": {
        "keywords": ["हार्वेस्ट डेज चुकल्यास", "harvest days missed impact", "उत्पन्नावर परिणाम"],
        "mr": "ऊस जास्त पिकल्यास (Over-ripening), साखरेचे प्रमाण कमी होऊ शकते आणि पिकाचा  'रिकव्हरी रेट' घटू शकतो , ज्यामुळे आर्थिक नुकसान होते.",
        "hi": "गन्ना ज्यादा पकने पर (Over-ripening), चीनी की मात्रा कम हो सकती है और फसल का  'रिकवरी रेट' घट सकता है , जिससे आर्थिक नुकसान होता है।",
        "en": "If sugarcane is over-ripened, the sugar content may decrease, and the crop's  'Recovery Rate' can drop , leading to financial loss."
    },
    "crop_status_suitability": {
        "keywords": ["क्रॉप स्टेटस योग्य आहे", "crop status suitability", "स्थिति सही है या नहीं"],
        "mr": "तुमच्या पीक स्थितीची तुलना CropEye.ai मधील त्याच हंगामातील  (Regional Best Practices) इष्टतम वाढीच्या टप्प्यांशी  केली जाते.",
        "hi": "आपकी फसल की स्थिति की तुलना CropEye.ai में उसी सीजन के  (Regional Best Practices) इष्टतम विकास चरणों  से की जाती है।",
        "en": "Your crop status is compared with the  optimal growth stages (Regional Best Practices)  for the same season within CropEye.ai."
    },
    "crop_status_manual_change": {
        "keywords": ["क्रॉप स्टेटस मी बदलू शकतो", "crop status manual change", "स्थिति खुद बदल सकते हैं"],
        "mr": "बहुतेक वेळा CropEye.ai ते आपोआप ठरवते, परंतु तुम्ही तुमच्या व्यवस्थापकाशी संपर्क साधून किंवा ॲपमध्ये आवश्यक इनपुट देऊन  बदल सुचवू शकता .",
        "hi": "अधिकांश समय CropEye.ai इसे स्वचालित रूप से निर्धारित करता है, लेकिन आप अपने प्रबंधक से संपर्क करके या ऐप में आवश्यक इनपुट देकर  बदलाव सुझा सकते हैं ।",
        "en": "Most of the time CropEye.ai determines it automatically, but you can  suggest changes  by contacting your manager or providing necessary input in the app."
    },
    "greeting": {
    "keywords": ["hello", "hii", "hi", "नमस्कार", "नमस्ते", "hey"],
    "mr": "नमस्कार! मी तुम्हाला कशात मदत करू शकतो?",
    "hi": "नमस्ते! मैं आपकी किस तरह मदद कर सकता हूँ?",
    "en": "Hello! How can I assist you today?"
    },

    # ----------------------------------------------------------------------
    # २. फील्ड इंडायसेस (Field Indices) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "growth_index_low_reason": {
        "keywords": ["ग्रोथ इंडेक्स कमी का", "growth index low reason", "ग्रोथ इंडेक्स कम क्यों"],
        "mr": "'ग्रोथ इंडेक्स' कमी होण्याची मुख्य कारणे म्हणजे  पाण्याची कमतरता , पोषक तत्वांची (उदा. नायट्रोजन) कमतरता किंवा पिकावर आलेला  ताण (Stress) .",
        "hi": "'ग्रोथ इंडेक्स' कम होने के मुख्य कारण  पानी की कमी , पोषक तत्वों (जैसे नाइट्रोजन) की कमी या फसल पर आया हुआ  तनाव (Stress)  हैं।",
        "en": "The main reasons for a low 'Growth Index' are  water deficit , lack of nutrients (e.g., Nitrogen), or  stress  on the crop."
    },
    "growth_index_optimal_level": {
        "keywords": ["ग्रोथ इंडेक्स कोणत्या पातळीवर", "growth index optimal level", "ग्रोथ इंडेक्स स्तर"],
        "mr": "पिकाच्या प्रकारानुसार आणि टप्प्यानुसार ही पातळी बदलते, परंतु शक्यतो हा निर्देशांक  उच्च पातळीवर (उदा. ०.७५ च्या वर)  आणि स्थिर राखणे फायदेशीर असते.",
        "hi": "फसल के प्रकार और चरण के अनुसार यह स्तर बदलता है, लेकिन इसे  उच्च स्तर (जैसे ०.७५ से ऊपर)  और स्थिर बनाए रखना फायदेमंद होता है।",
        "en": "This level varies by crop type and stage, but it is beneficial to maintain the index at a  high level (e.g., above 0.75)  and stable."
    },
    "growth_index_low_fertilizer": {
        "keywords": ["ग्रोथ इंडेक्स सुधारणा खत", "growth index fertilizer", "ग्रोथ इंडेक्स खाद", "युरिया"],
        "mr": "ग्रोथ इंडेक्स थेट  नायट्रोजनच्या कमतरतेशी  संबंधित असतो. त्यामुळे नायट्रोजनयुक्त खत (उदा. युरिया) त्वरित देण्याची शिफारस केली जाते.",
        "hi": "ग्रोथ इंडेक्स सीधे  नाइट्रोजन की कमी  से संबंधित होता है। इसलिए, नाइट्रोजन युक्त खाद (जैसे यूरिया) तुरंत देने की सिफारिश की जाती है।",
        "en": "The Growth Index is directly linked to  Nitrogen deficiency . Therefore, immediate application of Nitrogen-rich fertilizer (e.g., Urea) is recommended."
    },
    "growth_index_low_multi_reason": {
        "keywords": ["खताच्या कमतरतेमुळे की पाणी", "growth index multi reason", "ग्रोथ इंडेक्स कारण"],
        "mr": "हे  तिन्ही कारणामुळे  होऊ शकते. अचूक कारण ओळखण्यासाठी ग्रोथ इंडेक्सची तुलना 'वॉटर इंडेक्स' (पाणी) आणि 'स्ट्रेस इंडेक्स' (रोग/ताण) सोबत केली पाहिजे.",
        "hi": "यह  तीनों कारणों  से हो सकता है। सटीक कारण जानने के लिए ग्रोथ इंडेक्स की तुलना 'वॉटर इंडेक्स' (पानी) और 'स्ट्रेस इंडेक्स' (रोग/तनाव) के साथ की जानी चाहिए।",
        "en": "It can be due to  all three reasons . To identify the exact cause, the Growth Index must be compared with the 'Water Index' (water) and 'Stress Index' (disease/stress)."
    },
    "growth_index_biomass_relation": {
        "keywords": ["ग्रोथ इंडेक्स बायोमास संबंध", "growth index biomass relation", "बायोमास संबंध"],
        "mr": "'ग्रोथ इंडेक्स' (NDVI) हे पिकाच्या हिरवेपणाचे आणि घनतेचे मापन आहे. उच्च 'ग्रोथ इंडेक्स' म्हणजे  जास्त 'बायोमास'  आणि उच्च उत्पादन संभाव्यता.",
        "hi": "'ग्रोथ इंडेक्स' (NDVI) फसल के हरेपन और घनत्व का मापन है। उच्च 'ग्रोथ इंडेक्स' का अर्थ है  अधिक 'बायोमास'  और उच्च उत्पादन क्षमता।",
        "en": "The 'Growth Index' (NDVI) is a measure of crop greenness and density. A higher 'Growth Index' means  more 'Biomass'  and higher yield potential."
    },
    "stress_index_high_first_step": {
        "keywords": ["स्ट्रेस इंडेक्स वाढल्यास उपाययोजना", "stress index high first step", "स्ट्रेस इंडेक्स उपाय"],
        "mr": "'स्ट्रेस इंडेक्स' वाढल्यास प्रथम  मातीतील ओलावा तपासावा . पाण्याची कमतरता असल्यास  त्वरित सिंचन  सुरू करावे.",
        "hi": "'स्ट्रेस इंडेक्स' बढ़ने पर, सबसे पहले  मिट्टी की नमी जांचें । पानी की कमी होने पर  तुरंत सिंचाई  शुरू करें।",
        "en": "If the 'Stress Index' is high, first  check the soil moisture . If there is a water deficit,  start irrigation immediately ."
    },
    "stress_index_danger_zone": {
        "keywords": ["स्ट्रेस इंडेक्स धोक्याची घंटा", "stress index danger zone", "खतरे का स्तर"],
        "mr": "पिकाच्या प्रकारानुसार 'धोक्याची पातळी' बदलते, परंतु  उच्च पातळीवर (उदा. ०.५० च्या वर)  आणि सतत वाढत असलेला निर्देशांक त्वरित उपचाराची गरज दर्शवतो.",
        "hi": "फसल के प्रकार के अनुसार 'खतरे का स्तर' बदलता है, लेकिन  उच्च स्तर पर (जैसे ०.५० से ऊपर)  और लगातार बढ़ता हुआ इंडेक्स तत्काल उपचार की आवश्यकता दर्शाता है।",
        "en": "The 'danger level' varies by crop type, but an index at a  high level (e.g., above 0.50)  and continuously rising indicates an immediate need for treatment."
    },
    "stress_index_yield_loss": {
        "keywords": ["उच्च स्ट्रेस इंडेक्समुळे नुकसान", "stress index yield loss", "उत्पादनात घट"],
        "mr": "उच्च ताणामुळे प्रकाशसंश्लेषण (Photosynthesis) थांबते, पिकाची वाढ खुंटते आणि थेट  उत्पादनात (Yield) मोठी घट  होते.",
        "hi": "उच्च तनाव के कारण प्रकाश संश्लेषण (Photosynthesis) रुक जाता है, फसल की वृद्धि रुक जाती है और सीधे  उत्पादन (Yield) में भारी कमी  आती है।",
        "en": "High stress halts photosynthesis, stunts crop growth, and directly leads to a  significant decrease in yield ."
    },
    "stress_index_water_vs_heat": {
        "keywords": ["पाण्याची कमतरता की उष्णतेचा ताण", "water vs heat stress", "पानी की कमी या गर्मी का तनाव"],
        "mr": "पाण्याची कमतरता असल्यास 'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' दोन्ही कमी झालेले दिसतील, तर फक्त उष्णतेचा ताण असल्यास फक्त  पानांचे तापमान वाढलेले  दिसेल (थर्मल स्ट्रेस).",
        "hi": "पानी की कमी होने पर 'वॉटर इंडेक्स' और 'मॉइश्चर इंडेक्स' दोनों कम दिखेंगे, जबकि केवल गर्मी का तनाव होने पर केवल  पत्तियों का तापमान बढ़ा हुआ  दिखेगा (थर्मल स्ट्रेस)।",
        "en": "Water deficit will show low 'Water Index' and 'Moisture Index', whereas only heat stress will show  increased leaf temperature  (Thermal Stress)."
    },
    "stress_index_disease_detection": {
        "keywords": ["स्ट्रेस इंडेक्स रोग ओळखू शकतो", "stress index disease detection", "रोग पहचान"],
        "mr": "'स्ट्रेस इंडेक्स' पानांच्या रंग आणि संरचनेतील बदलांवरून  रोगांमुळे आलेला ताण  (उदा. बुरशीजन्य रोग) ओळखू शकतो, परंतु विशिष्ट रोगाचे नाव देण्यासाठी त्याला अधिक विश्लेषणाची गरज असते.",
        "hi": "'स्ट्रेस इंडेक्स' पत्तियों के रंग और संरचना में बदलाव से  रोगों के कारण हुए तनाव  (जैसे फंगल रोग) को पहचान सकता है, लेकिन विशिष्ट रोग का नाम बताने के लिए उसे अधिक विश्लेषण की आवश्यकता होती है।",
        "en": "The 'Stress Index' can identify  stress caused by diseases  (e.g., fungal diseases) based on changes in leaf color and structure, but requires more analysis to name the specific disease."
    },
    "water_vs_moisture_index": {
        "keywords": ["वॉटर इंडेक्स मॉईश्चर इंडेक्स फरक", "water moisture index difference", "पानी और नमी सूचकांक"],
        "mr": " 'वॉटर इंडेक्स'  पिकाच्या  पानांमधील पाण्याची मात्रा  दर्शवतो, तर  'मॉईश्चर इंडेक्स'   मातीतील ओलाव्याचे प्रमाण  दर्शवतो.",
        "hi": " 'वॉटर इंडेक्स'  फसल की  पत्तियों में पानी की मात्रा  दर्शाता है, जबकि  'मॉइश्चर इंडेक्स'   मिट्टी की नमी की मात्रा  दर्शाता है।",
        "en": "The  'Water Index'  shows the  amount of water in the crop leaves , while the  'Moisture Index'  shows the  amount of moisture in the soil ."
    },
    "moisture_index_irrigation_level": {
        "keywords": ["मॉईश्चर इंडेक्स सिंचन पातळी", "moisture index irrigation level", "नमी सूचकांक सिंचाई"],
        "mr": "जेव्हा 'मॉईश्चर इंडेक्स'  ५०% च्या खाली  जातो, तेव्हा  त्वरित सिंचनाची  शिफारस केली जाते.",
        "hi": "जब 'मॉइश्चर इंडेक्स'  ५०% से नीचे  चला जाता है, तब  तुरंत सिंचाई  करने की सिफारिश की जाती है।",
        "en": "When the 'Moisture Index' drops  below 50% ,  immediate irrigation  is recommended."
    },
    "moisture_index_soil_type": {
        "keywords": ["मातीचा प्रकार मॉईश्चर इंडेक्सवर परिणाम", "soil type moisture index impact", "मिट्टी का प्रकार"],
        "mr": "रेताड माती लवकर पाणी गमावते, तर काळी माती पाणी जास्त काळ टिकवून ठेवते. त्यामुळे  मातीच्या प्रकारानुसार  इंडेक्सची 'धोक्याची पातळी' निश्चित करावी लागते.",
        "hi": "रेतीली मिट्टी जल्दी पानी खो देती है, जबकि काली मिट्टी पानी को लंबे समय तक बनाए रखती है। इसलिए  मिट्टी के प्रकार के अनुसार  इंडेक्स का 'खतरे का स्तर' तय करना पड़ता है।",
        "en": "Sandy soil loses water quickly, while black soil retains water longer. Therefore, the index's 'danger level' must be set  according to the soil type ."
    },
    "water_index_rain_change": {
        "keywords": ["जोरदार पाऊस वॉटर इंडेक्स बदल", "water index rain change", "बारिश के बाद इंडेक्स"],
        "mr": "'वॉटर इंडेक्स' (पानांमधील पाणी) पाऊस थांबल्यानंतर  काही तासांत लगेच सुधारू लागतो , कारण पिके त्वरित पाणी शोषण्यास सुरुवात करतात.",
        "hi": "वॉटर इंडेक्स' (पत्तियों में पानी) बारिश रुकने के बाद  कुछ ही घंटों में तुरंत सुधरने लगता है , क्योंकि फसलें तुरंत पानी सोखना शुरू कर देती हैं।",
        "en": "The 'Water Index' (water in leaves) starts to  improve immediately within a few hours  after the rain stops, as crops start absorbing water quickly."
    },
    "water_index_no_improvement": {
        "keywords": ["सिंचन केल्यावरही वॉटर इंडेक्स सुधारत नाही", "water index no improvement", "सिंचाई के बाद भी"],
        "mr": "याचा अर्थ मुळांना पाणी शोषण्यात अडचण येत आहे. हे कदाचित  माती घट्ट झाल्यामुळे (Compaction)  किंवा मुळांना रोग झाल्यामुळे असू शकते.",
        "hi": "इसका मतलब है कि जड़ों को पानी सोखने में दिक्कत आ रही है। यह शायद  मिट्टी के सख्त होने (Compaction)  या जड़ों में रोग होने के कारण हो सकता है।",
        "en": "This means the roots are having trouble absorbing water. This may be due to  soil compaction  or root diseases."
    },
    # ----------------------------------------------------------------------
    # ३. माती, आरोग्य आणि बायोमास (Soil, Health & Biomass) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "organic_carbon_optimal": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी किती", "organic carbon optimal level", "सेंद्रिय कर्ब", "organic carbon density"],
        "mr": "साधारणपणे, सेंद्रिय कर्बाचे प्रमाण  ०.५% पेक्षा जास्त  (म्हणजेच gm/cm³ मध्ये जास्त) असल्यास मातीची गुणवत्ता चांगली मानली जाते.",
        "hi": "सामान्यतः, यदि कार्बनिक कार्बन की मात्रा  ०.५% से अधिक  (यानी gm/cm³ में अधिक) है तो मिट्टी की गुणवत्ता अच्छी मानी जाती है।",
        "en": "Generally, soil quality is considered good if the organic carbon content is  greater than 0.5%  (i.e., higher in gm/cm³)."
    },
    "organic_carbon_improve": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी सुधारण्यासाठी खत", "improve organic carbon", "सेंद्रिय खत"],
        "mr": " शेणखत, कंपोस्ट खत, गांडूळ खत  किंवा हिरवळीची खते (Green Manure) वापरून 'ऑरगॅनिक कार्बन डेन्सिटी' सुधारता येते.",
        "hi": " गोबर की खाद, कंपोस्ट खाद, केंचुआ खाद  या हरी खाद (Green Manure) का उपयोग करके 'कार्बनिक कार्बन घनत्व' में सुधार किया जा सकता है।",
        "en": " Cow dung manure, compost, vermicompost,  or green manures can be used to improve 'Organic Carbon Density'."
    },
    "soil_ph_sugarcane_optimal": {
        "keywords": ["pH लेव्हल ऊस पिकासाठी योग्य आहे", "soil ph level sugarcane", "pH 7.30"],
        "mr": " ७.३० pH  ऊस पिकासाठी स्वीकार्य आहे (ऊस ६.० ते ८.५ pH मध्ये वाढतो). pH जास्त असल्यास  गंधक (Sulphur)  वापरावा आणि कमी असल्यास  चुना (Lime)  वापरावा.",
        "hi": " ७.३० pH  गन्ने की फसल के लिए स्वीकार्य है (गन्ना ६.० से ८.५ pH में बढ़ता है)। pH अधिक होने पर  सल्फर (Sulphur)  का उपयोग करें और कम होने पर  चूना (Lime)  का उपयोग करें।",
        "en": " 7.30 pH  is acceptable for sugarcane (sugarcane grows in 6.0 to 8.5 pH). Use  Sulphur  if the pH is high and  Lime  if it is low."
    },
    "biomass_yield_projection_relation": {
        "keywords": ["बायोमास उत्पादन अंदाज संबंध", "biomass yield projection relation", "कुल बायोमास"],
        "mr": "'एकूण बायोमास' हे पिकाच्या वाढीचे वर्तमान वजन आहे, जे 'उत्पादन अंदाजा'साठी आधारभूत आहे.  जास्त बायोमास म्हणजे जास्त उत्पादन  मिळण्याची शक्यता.",
        "hi": "'कुल बायोमास' फसल की वृद्धि का वर्तमान वजन है, जो 'उत्पादन अनुमान' के लिए आधार है।  अधिक बायोमास का अर्थ है अधिक उत्पादन  मिलने की संभावना।",
        "en": "Total Biomass is the current weight of crop growth, which is the basis for the 'Yield Projection'.  More biomass means a higher probability of higher yield ."
    },
    "biomass_distribution_measurement": {
        "keywords": ["बायोमासचे वितरण", "biomass distribution measurement", "जमिनीवरील जमिनीखालील"],
        "mr": "हे विशिष्ट पिकाच्या  'वाढीच्या मॉडेल'वर आधारित AI अल्गोरिदमद्वारे  उपग्रह डेटाचे विश्लेषण करून  अंदाजित  केले जाते.",
        "hi": "यह विशिष्ट फसल के  'विकास मॉडल' पर आधारित AI एल्गोरिदम  द्वारा उपग्रह डेटा का विश्लेषण करके  अनुमानित  किया जाता है।",
        "en": "This is  estimated  by  AI algorithms based on the specific crop's 'growth model'  by analyzing satellite data."
    },
    "stress_events_zero": {
        "keywords": ["स्ट्रेस इव्हेंट्स शून्य आहेत", "stress events zero", "तनाव घटनाएं शून्य"],
        "mr": "शून्य 'स्ट्रेस इव्हेंट्स' म्हणजे सध्या कोणतेही मोठे धोके नाहीत. तथापि, 'ग्रोथ इंडेक्स' स्थिर किंवा कमी होत असल्यास,  सूक्ष्म कमतरता (Micro-Deficiency)  असू शकते.",
        "hi": "शून्य 'तनाव घटनाओं' का मतलब है कि वर्तमान में कोई बड़ा खतरा नहीं है। हालांकि, यदि 'ग्रोथ इंडेक्स' स्थिर या कम हो रहा है, तो  सूक्ष्म कमी (Micro-Deficiency)  हो सकती है।",
        "en": "Zero 'Stress Events' means there are no major risks currently. However, if the 'Growth Index' is stable or decreasing, there might be a  Micro-Deficiency ."
    },
    "recovery_rate_low_comparison": {
        "keywords": ["रिकव्हरी रेट कमी का", "recovery rate low reason", "रिकवरी रेट कम क्यों"],
        "mr": "'रिकव्हरी रेट' साखरेच्या गुणवत्तेवर आणि जातीवर अवलंबून असतो. जरी तो प्रादेशिक सरासरीपेक्षा चांगला असला तरी, तो अजूनही  'इष्टतम पातळी' (Optimal Level) पर्यंत पोहोचलेला नाही .",
        "hi": "'रिकवरी रेट' चीनी की गुणवत्ता और किस्म पर निर्भर करता है। भले ही यह क्षेत्रीय औसत से बेहतर हो, यह अभी भी  'इष्टतम स्तर' (Optimal Level) तक नहीं पहुंचा है ।",
        "en": "The 'Recovery Rate' depends on sugar quality and variety. Even if it is better than the regional average, it still  hasn't reached the 'Optimal Level' ."
    },
    "recovery_rate_improve_potash": {
        "keywords": ["रिकव्हरी रेट सुधारण्यासाठी उपाय", "improve recovery rate", "पोटॅश", "potash"],
        "mr": "'रिकव्हरी रेट' वाढवण्यासाठी पिकाच्या योग्य टप्प्यावर  पोटॅश (Potash) आणि सल्फर (Sulphur)  सारख्या पोषक तत्वांचा योग्य प्रमाणात वापर करणे महत्त्वाचे आहे.",
        "hi": "'रिकवरी रेट' बढ़ाने के लिए फसल के सही चरण में  पोटाश (Potash) और सल्फर (Sulphur)  जैसे पोषक तत्वों का सही मात्रा में उपयोग करना महत्वपूर्ण है।",
        "en": "To increase the 'Recovery Rate', it is important to use the right amount of nutrients like  Potash and Sulphur  at the appropriate crop stage."
    },
    "biomass_decrease_causes": {
        "keywords": ["बायोमास कमी होऊ शकतो", "biomass decrease causes", "बायोमास कम होने के कारण"],
        "mr": " पाण्याचा ताण, पोषक तत्वांची कमतरता , अपुरा सूर्यप्रकाश किंवा रोग/कीटकांचा प्रादुर्भाव यांमुळे 'बायोमास' कमी होऊ शकतो.",
        "hi": " पानी का तनाव, पोषक तत्वों की कमी , अपर्याप्त धूप या रोग/कीटों का प्रकोप के कारण 'बायोमास' कम हो सकता है।",
        "en": "'Biomass' can decrease due to  water stress, nutrient deficiency , insufficient sunlight, or pest/disease infestation."
    },
    "soil_ph_nutrient_relation": {
        "keywords": ["pH पोषक तत्वांची उपलब्धता", "ph nutrient relation", "pH और पोषक तत्व"],
        "mr": "मातीचा pH योग्य असल्यास (उदा. ६.५ ते ७.५),  नायट्रोजन, फॉस्फरस आणि पोटॅशसह बहुतेक पोषक तत्त्वे  पिकांसाठी सहज उपलब्ध होतात. pH बदलल्यास उपलब्धता कमी होते.",
        "hi": "यदि मिट्टी का pH सही है (जैसे ६.५ से ७.५), तो  नाइट्रोजन, फास्फोरस और पोटाश सहित अधिकांश पोषक तत्व  फसलों के लिए आसानी से उपलब्ध होते हैं। pH बदलने पर उपलब्धता कम हो जाती है।",
        "en": "If the soil pH is correct (e.g., 6.5 to 7.5),  most nutrients, including Nitrogen, Phosphorus, and Potash , are readily available to crops. Availability decreases if the pH changes."
    },
    # ----------------------------------------------------------------------
    # ४. उत्पादन आणि कार्यक्षमता (Yield & Performance) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "projected_vs_optimal_yield": {
        "keywords": ["प्रोजेक्टेड यील्ड कमी का", "projected vs optimal yield", "उत्पादन अनुमान कम क्यों"],
        "mr": "'प्रोजेक्टेड यील्ड' तुमच्या सध्याच्या व्यवस्थापन आणि वाढीच्या स्थितीवर आधारित आहे, तर 'ऑप्टिमल यील्ड' हे  सर्वात चांगल्या परिस्थितीत  शक्य असलेले उत्पादन आहे.",
        "hi": "'प्रोजेक्टेड यील्ड' आपके वर्तमान प्रबंधन और वृद्धि की स्थिति पर आधारित है, जबकि 'ऑप्टिमल यील्ड'  सर्वोत्तम परिस्थितियों  में संभव उत्पादन है।",
        "en": "'Projected Yield' is based on your current management and growth status, while 'Optimal Yield' is the production possible under  the best possible conditions ."
    },
    "optimal_yield_management_changes": {
        "keywords": ["ऑप्टिमल यील्ड पर्यंत पोहोचण्यासाठी", "optimal yield management changes", "सर्वोत्तम उत्पादन के लिए"],
        "mr": " सिंचन, खतांचे वेळापत्रक आणि योग्य जातीची निवड  सुधारून, तसेच तणावाचे प्रमाण कमी करून हे बदल करता येतात.",
        "hi": " सिंचाई, उर्वरक अनुसूची और सही किस्म के चयन  में सुधार करके, साथ ही तनाव की मात्रा को कम करके ये बदलाव किए जा सकते हैं।",
        "en": "These changes can be made by improving  irrigation, fertilizer scheduling, and selection of the right variety , as well as reducing the amount of stress."
    },
    "performance_action_plan": {
        "keywords": ["परफॉर्मन्स वाढवण्यासाठी कृती योजना", "performance action plan", "कार्यक्षमता बढ़ाने के लिए"],
        "mr": "पुढील तीन महिन्यांसाठी 'ग्रोथ इंडेक्स' सुधारण्यासाठी  खतांचा आणि पाण्याची गरज पूर्ण करणारी शिफारस केलेली कृती योजना  (Recommended Action Plan) वापरावी.",
        "hi": "अगले तीन महीनों के लिए 'ग्रोथ इंडेक्स' में सुधार के लिए  खाद और पानी की जरूरतें पूरी करने वाली अनुशंसित कार्य योजना  (Recommended Action Plan) का उपयोग करें।",
        "en": "Use the  Recommended Action Plan  that meets the fertilizer and water needs to improve the 'Growth Index' for the next three months."
    },
    "low_yield_high_recovery": {
        "keywords": ["रिकव्हरी रेट चांगला असूनही उत्पादन कमी", "high recovery low yield", "रिकवरी रेट अच्छा फिर भी"],
        "mr": "'रिकव्हरी रेट' (गुणवत्ता) चांगला असला तरी, तुमचा  'एकूण बायोमास' कमी  असेल, तर एकूण उत्पादन (Total Quantity) कमीच राहील.",
        "hi": "'रिकवरी रेट' (गुणवत्ता) अच्छा होने के बावजूद, यदि आपका  'कुल बायोमास' कम  है, तो कुल उत्पादन (Total Quantity) कम ही रहेगा।",
        "en": "Even if the 'Recovery Rate' (quality) is good, if your  'Total Biomass' is low , the total yield (Total Quantity) will remain low."
    },
    "yield_increase_irrigation_vs_fertilizer": {
        "keywords": ["उत्पादन वाढवण्यासाठी सिंचन की खते", "irrigation vs fertilizer for yield", "सिंचाई या खाद"],
        "mr": "प्रथम  'वॉटर इंडेक्स' आणि 'ग्रोथ इंडेक्स' तपासा . जर दोन्ही कमी असतील, तर दोन्ही आवश्यक आहेत. फक्त ग्रोथ कमी असेल तर खत आवश्यक आहे.",
        "hi": "पहले  'वॉटर इंडेक्स' और 'ग्रोथ इंडेक्स' जांचें । यदि दोनों कम हैं, तो दोनों आवश्यक हैं। यदि केवल ग्रोथ कम है तो खाद आवश्यक है।",
        "en": "First,  check the 'Water Index' and 'Growth Index' . If both are low, both are necessary. If only Growth is low, fertilizer is necessary."
    },
    "yield_projection_accuracy": {
        "keywords": ["यील्ड प्रोजेक्शनची अचूकता", "yield projection accuracy", "उत्पादन अनुमान की सटीकता"],
        "mr": "हे AI मॉडेलची अचूकता (Accuracy)  ९०% किंवा त्याहून अधिक  असते, परंतु हवामानातील मोठे आणि अनपेक्षित बदल या अंदाजावर परिणाम करू शकतात.",
        "hi": "इस AI मॉडल की सटीकता (Accuracy)  ९०% या उससे अधिक  होती है, परंतु मौसम में बड़े और अप्रत्याशित बदलाव इस अनुमान को प्रभावित कर सकते हैं।",
        "en": "The accuracy of this AI model is  90% or higher , but large and unexpected changes in weather can affect this prediction."
    },
    "low_yield_area_map": {
        "keywords": ["उत्पादन कमी येण्याची शक्यता नकाशावर", "low yield area map", "कम उत्पादन वाला क्षेत्र"],
        "mr": "होय, CropEye.ai  'झोन मॅनेजमेंट' (Zone Management) नकाशावर  'ग्रोथ इंडेक्स' सर्वात कमी असलेल्या भागांना चिन्हांकित करून दाखवते, जिथे उत्पादन कमी असेल.",
        "hi": "हाँ, CropEye.ai  'ज़ोन मैनेजमेंट' (Zone Management) मानचित्र  पर 'ग्रोथ इंडेक्स' सबसे कम वाले क्षेत्रों को चिह्नित करके दिखाता है, जहाँ उत्पादन कम होगा।",
        "en": "Yes, CropEye.ai shows areas with the lowest 'Growth Index' by marking them on the  'Zone Management' map , indicating where the yield will be low."
    },
    # ----------------------------------------------------------------------
    # ५. कृती आणि निर्णय समर्थन (Action & Decision Support) संबंधित प्रश्न
    # ----------------------------------------------------------------------
    "irrigation_event_impact": {
        "keywords": ["सिंचन इव्हेंट्स वॉटर इंडेक्सवर परिणाम", "irrigation events water index impact", "सिंचाई का प्रभाव"],
        "mr": "सिंचन इव्हेंट्स वाढवल्यास  'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' लगेच वाढतात , ज्यामुळे पिकाचा ताण कमी होतो.",
        "hi": "सिंचन इव्हेंट्स वाढवल्यास  'वॉटर इंडेक्स' आणि 'मॉईश्चर इंडेक्स' लगेच वाढतात , ज्यामुळे पिकाचा ताण कमी होतो.",
        "en": "Increasing irrigation events  immediately raises the 'Water Index' and 'Moisture Index' , which reduces crop stress."
    },
    "weather_forecast_irrigation_planning": {
        "keywords": ["७ दिवसांच्या हवामान अंदाजानुसार सिंचन नियोजन", "weather forecast irrigation planning", "मौसम अनुमान सिंचाई"],
        "mr": "जर पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "hi": "यदि पुढील ४८ तासांत जोरदार पावसाचा अंदाज असेल, तर  सिंचन थांबवावे . जर तापमान वाढणार असेल, तर सिंचनाची मात्रा वाढवावी.",
        "en": "If heavy rain is forecast in the next 48 hours,  stop irrigation . If the temperature is going to rise, increase the amount of irrigation."
    },
    "file_report_records": {
        "keywords": ["फाइल रिपोर्ट मध्ये नोंदी", "file report records", "फाइल रिपोर्ट में रिकॉर्ड"],
        "mr": "तुम्ही  खतांचा वापर, फवारणी, सिंचनाच्या वेळा, मजुरीचा खर्च  आणि इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "hi": "आप  खाद का उपयोग, छिड़काव, सिंचाई का समय, मजदूरी का खर्च  और इतर सर्व शेतातील क्रियाकलापांच्या नोंदी ठेवू शकता.",
        "en": "You can keep records of  fertilizer usage, spraying, irrigation times, labor costs , and all other farm activities."
    },
    "sales_report_impact": {
        "keywords": ["सेल्स रिपोर्ट भरल्याने फरक", "sales report impact", "बिक्री रिपोर्ट का प्रभाव"],
        "mr": "'सेल्स रिपोर्ट' थेट डॅशबोर्डवरील डेटा (उदा. इंडेक्स) बदलत नाही, परंतु तुमच्या  आर्थिक अहवालावर (Financial Report)  आणि उत्पादन विश्लेषणामध्ये (Yield Analysis) मदत करतो.",
        "hi": "'सेल्स रिपोर्ट' थेट डॅशबोर्डवरील डेटा (उदा. इंडेक्स) बदलत नाही, परंतु तुमच्या  आर्थिक अहवालावर (Financial Report)  आणि उत्पादन विश्लेषणामध्ये (Yield Analysis) मदत करतो.",
        "en": "The 'Sales Report' does not directly change the data on the dashboard (e.g., indices), but it helps with your  Financial Report  and Yield Analysis."
    },
    "dashboard_alerts_phone": {
        "keywords": ["सूचना फोनवर मेसेजद्वारे", "dashboard alerts phone", "अलर्ट मैसेज"],
        "mr": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "hi": "होय, CropEye.ai ॲप तुम्हाला  'सिंचनाची गरज'  किंवा  'तणावाचा धोका'  अशा महत्त्वाच्या सूचना (Alerts) थेट फोनवर मेसेज किंवा नोटिफिकेशनद्वारे पाठवण्याची सुविधा देते.",
        "en": "Yes, the CropEye.ai app allows you to send important Alerts like  'Irrigation Need'  or  'Stress Risk'  directly to your phone via message or notification."
    },
    "historical_data_comparison": {
        "keywords": ["मागील वर्षाच्या डेटा सोबत तुलना", "historical data comparison", "पिछले साल का डेटा"],
        "mr": "डॅशबोर्डवर  'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "hi": "डॅशबोर्डवर  'इयरली' (Yearly) किंवा 'तुलना' (Comparison)  पर्याय निवडून तुम्ही ग्रोथ इंडेक्स, स्ट्रेस इंडेक्स आणि उत्पादन अंदाजाची तुलना करू शकता.",
        "en": "You can compare the Growth Index, Stress Index, and Yield Projection by selecting the  'Yearly' or 'Comparison'  option on the dashboard."
    },
    "fertilizer_recommendation": {
        "keywords": ["कोणत्या विशिष्ट खतांची गरज", "fertilizer recommendation NPK", "खाद की सिफारिश"],
        "mr": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "hi": "होय, 'ग्रोथ इंडेक्स' आणि माती pH स्तराचे विश्लेषण करून डॅशबोर्ड  NPK आणि सूक्ष्म पोषक तत्वांची (Micro-Nutrients)  शिफारस करतो.",
        "en": "Yes, by analyzing the 'Growth Index' and soil pH level, the dashboard recommends  NPK and Micro-Nutrients ."
    },
    "recovery_rate_advisor": {
        "keywords": ["रिकव्हरी रेट कमी असल्यास कृषी सल्लागार", "recovery rate advisor", "कृषि सलाहकार"],
        "mr": "'रिकव्हरी रेट' (साखरेची गुणवत्ता) सुधारण्यासाठी तुम्हाला  ऊस पिकातील पोषण आणि व्यवस्थापनाचा अनुभव  असलेल्या कृषी तज्ञाची मदत घ्यावी लागेल.",
        "hi": "'रिकव्हरी रेट' (साखरेची गुणवत्ता) सुधारण्यासाठी तुम्हाला  ऊस पिकातील पोषण आणि व्यवस्थापनाचा अनुभव  असलेल्या कृषी तज्ञाची मदत घ्यावी लागेल.",
        "en": "To improve the 'Recovery Rate' (sugar quality), you will need the help of an agricultural expert who has  experience in nutrition and management of sugarcane crops ."
    },
    # ----------------------------------------------------------------------
    # नवीन डॅशबोर्ड कंपोनंट्सची माहिती Q&A म्हणून जोडत आहोत (Dashboard Components Benefits)
    # ----------------------------------------------------------------------
    "field_area_benefit": {
        "keywords": ["फील्ड एरिया फायदा", "field area benefit", "क्षेत्रफल लाभ"],
        "mr": "फील्ड एरियामुळे पेरणी, खत आणि सिंचन यासाठी  प्रति एकर खर्चाचे अचूक आणि सोपे नियोजन  करता येते.",
        "hi": "फील्ड एरियामुळे पेरणी, खत आणि सिंचन यासाठी  प्रति एकर खर्चाचे अचूक आणि सोपे नियोजन  करता येते.",
        "en": "Field Area allows for  accurate and easy planning of cost per acre  for planting, fertilizer, and irrigation."
    },
    "crop_status_benefit": {
        "keywords": ["पीक स्थिती फायदा", "benefit","crop status benefit", "फसल स्थिति लाभ"],
        "mr": "पीक स्थितीमुळे पिकाच्या गरजेनुसार व्यवस्थापनाचे निर्णय (उदा. फवारणी, पाणी थांबवणे) घेण्यासाठी  वेळेची अचूकता  मिळते.",
        "hi": "पीक स्थितीमुळे पिकाच्या गरजेनुसार व्यवस्थापनाचे निर्णय (उदा. फवारणी, पाणी थांबवणे) घेण्यासाठी  वेळेची अचूकता  मिळते.",
        "en": "Crop Status provides  timing accuracy  for making management decisions (e.g., spraying, stopping water) according to the crop's needs."
    },
    "days_to_harvest_benefit": {
        "keywords": ["कापणीसाठीचे दिवस फायदा", "harvest","days to harvest benefit", "कटाई के दिन लाभ"],
        "mr": "कापणीच्या दिवसांमुळे मजूर, वाहतूक आणि विक्रीचे नियोजन वेळेवर सुरू करून  काढणीची प्रक्रिया सुलभ  करता येते.",
        "hi": "कापणीच्या दिवसांमुळे मजूर, वाहतूक आणि विक्रीचे नियोजन वेळेवर सुरू करून  काढणीची प्रक्रिया सुलभ  करता येते.",
        "en": "Days to Harvest allows  simplification of the harvesting process  by starting timely planning for labor, transport, and sales."
    },
    "sugar_content_benefit": {
        "keywords": ["साखर सामग्री फायदा","sugar","sugar content benefit", "चीनी की सामग्री लाभ"],
        "mr": "साखर सामग्रीमुळे सर्वात योग्य वेळी कापणीचा निर्णय घेणे, जेणेकरून कारखान्यात ऊस पाठवल्यावर  जास्तीत जास्त रिकव्हरी  मिळेल.",
        "hi": "साखर सामग्रीमुळे सर्वात योग्य वेळी कापणीचा निर्णय घेणे, जेणेकरून कारखान्यात ऊस पाठवल्यावर  जास्तीत जास्त रिकव्हरी  मिळेल.",
        "en": "Sugar Content allows the decision for harvest at the most appropriate time, ensuring  maximum recovery  when sending sugarcane to the factory."
    },
    "indices_snapshot_benefit": {
        "keywords": ["इंडायसेस झलक फायदा", "indices snapshot benefit", "सूचकांक लाभ"],
        "mr": "फील्ड इंडायसेसमुळे पिकाचे आरोग्य एका दृष्टिक्षेपात समजते आणि खत, पाणी किंवा तणाव यापैकी  कोणती समस्या आहे हे त्वरित कळते .",
        "hi": "फील्ड इंडायसेसमुळे पिकाचे आरोग्य एका दृष्टिक्षेपात समजते आणि खत, पाणी किंवा तणाव यापैकी  कोणती समस्या आहे हे त्वरित कळते ।",
        "en": "Field Indices allow quick understanding of crop health and immediate identification of whether the problem is fertilizer, water, or stress-related."
    },
    "organic_carbon_density_benefit": {
        "keywords": ["ऑरगॅनिक कार्बन डेन्सिटी फायदा", "organic carbon benefit", "oc","सेंद्रिय कर्ब लाभ"],
        "mr": "ऑरगॅनिक कार्बन डेन्सिटीमुळे जमिनीची सुपीकता सुधारण्यासाठी  सेंद्रिय खते आणि पीक अवशेष व्यवस्थापनाचे निर्णय  घेण्यासाठी आधार मिळतो.",
        "hi": "ऑरगॅनिक कार्बन डेन्सिटीमुळे जमिनीची सुपीकता सुधारण्यासाठी  सेंद्रिय खते आणि पीक अवशेष व्यवस्थापनाचे निर्णय  घेण्यासाठी आधार मिळतो।",
        "en": "Organic Carbon Density provides the basis for making  decisions on organic fertilizers and crop residue management  to improve soil fertility."
    },
    "stress_events_benefit": {
        "keywords": ["तणाव घटना फायदा", "stress events benefit","stress", "तनाव घटनाएं लाभ"],
        "mr": "तणाव घटनांमुळे जोखीम कमी करण्यासाठी (Risk Mitigation) आणि भविष्यात तणाव टाळण्यासाठी  व्यवस्थापनात सुधारणा  करणे शक्य होते.",
        "hi": "तणाव घटनांमुळे जोखीम कमी करण्यासाठी (Risk Mitigation) आणि भविष्यात तणाव टाळण्यासाठी  व्यवस्थापनात सुधारणा  करणे शक्य होते।",
        "en": "Stress Events enable  improvement in management  to mitigate risk and prevent stress in the future."
    },
    "soil_ph_level_benefit": {
        "keywords": ["मातीचा pH स्तर फायदा", "soil ph benefit", "pH स्तर लाभ","soil"],
        "mr": "मातीचा pH स्तर योग्य असल्यास आवश्यकतेनुसार माती सुधारक (उदा. चुना, जिप्सम) वापरून  पोषक तत्वांची उपलब्धता वाढवता येते .",
        "hi": "मातीचा pH स्तर योग्य असल्यास आवश्यकतेनुसार माती सुधारक (उदा. चुना, जिप्सम) वापरून  पोषक तत्वांची उपलब्धता वाढवता येते ।",
        "en": "When the soil pH level is correct, the availability of nutrients can be increased by using soil amendments (e.g., lime, gypsum) as needed."
    },
    "yield_projection_benefit": {
        "keywords": ["उत्पादन अंदाज फायदा","yield", "yield projection benefit", "उत्पादन अनुमान लाभ"],
        "mr": "उत्पादन अंदाजामुळे बाजारातील धोरणे (Market Strategy) लवकर निश्चित करून  चांगला दर मिळवण्याचा प्रयत्न  करणे शक्य होते.",
        "hi": "उत्पादन अंदाजामुळे बाजारातील धोरणे (Market Strategy) लवकर निश्चित करून  चांगला दर मिळवण्याचा प्रयत्न  करणे शक्य होते।",
        "en": "Yield Projection allows for early determination of market strategies to  attempt to get a better price ."
    },
    "recovery_rate_comparison_benefit": {
        "keywords": ["रिकव्हरी रेट तुलना फायदा", "recovery","recovery rate comparison benefit", "रिकवरी रेट तुलना लाभ"],
        "mr": "रिकव्हरी रेट तुलना केल्याने तुमचा साखर गुणवत्ता दर सरासरीपेक्षा चांगला आहे की नाही हे समजते, ज्यामुळे  व्यवस्थापन सुधारण्यास मदत  होते.",
        "hi": "रिकव्हरी रेट तुलना केल्याने तुमचा साखर गुणवत्ता दर सरासरीपेक्षा चांगला आहे की नाही हे समजते, ज्यामुळे  व्यवस्थापन सुधारण्यास मदत  होते।",
        "en": "Recovery Rate Comparison helps determine if your sugar quality rate is better than the average, which  helps improve management ."
    },
    "cropeye_features": {
        "keywords": ["cropeye features", "features","features cropeye", "फीचर्स cropeye", "cropeye काय करते", "cropeye क्या करता है"],
        "mr": "CropEye उपग्रह, AI, पाणी-ताण, माती-नकाशे, कीड अलर्ट, हवामान अंदाज आणि उत्पादन अंदाज अशा स्मार्ट शेती फीचर्स देते.",
        "hi": "CropEye सैटेलाइट, AI, पानी तनाव, मिट्टी मैपिंग, कीट अलर्ट, मौसम पूर्वानुमान और उपज अनुमान जैसे स्मार्ट फीचर्स देता है.",
        "en": "CropEye offers smart features like satellite-based monitoring, AI insights, water stress detection, soil mapping, pest alerts, weather forecasts, and yield estimation."
    },
    "cropeye_benefits": {
        "keywords": ["cropeye benefits","benefits", "benefits cropeye", "cropeye फायदे", "cropeye लाभ", "why cropeye"],
        "mr": "CropEye चा फायदा म्हणजे जास्त उत्पादन, कमी खर्च, वेळेत अलर्ट, संसाधनांचा अचूक वापर आणि शेती व्यवस्थापन सुधारणा.",
        "hi": "CropEye के फ़ायदे हैं—ज्यादा उत्पादन, कम खर्च, समय पर अलर्ट, इनपुट की बचत और बेहतर खेत प्रबंधन.",
        "en": "CropEye benefits include higher yield, lower cost, timely alerts, optimized resource use, and improved farm management."
    },

    "productivity_benefit": {
        "keywords": ["productivity increase", "productivity","उत्पादन बढ़े कैसे", "yield improve", "उत्पादन फायदे", "more yield"],
        "mr": "लवकर समस्या ओळखल्यामुळे आणि संसाधनांचा योग्य वापर केल्यामुळे उत्पादन वाढते.",
        "hi": "समस्या जल्दी पहचानने और सही इनपुट उपयोग से फसल उत्पादन बढ़ता है.",
        "en": "Early issue detection and optimized inputs help increase productivity."
    },

    "C_saving_benefit": {
        "keywords": ["cost saving","risk reduce", "खर्च कमी", "input save", "water fertilizer save", "कम लागत खेती"],
        "mr": "अचूक सिंचन आणि खत व्यवस्थापनामुळे पाणी, खत आणि श्रम यांचा खर्च कमी होतो.",
        "hi": "सटीक सिंचाई और खाद प्रबंधन से पानी, खाद और श्रम की लागत कम होती है.",
        "en": "Precision irrigation and fertiliser planning reduce water, input, and labour costs."
    },

    "risk_reduction_benefit": {
        "keywords": ["risk reduce", "risk","फसल जोखिम", "crop loss prevent", "damage alert", "कीट रोग नुकसान"],
        "mr": "हवामान, कीड आणि रोग अलर्टमुळे मोठे नुकसान टाळता येते.",
        "hi": "मौसम, रोग और कीट अलर्ट से खेत में बड़े नुकसान को रोका जा सकता है.",
        "en": "Weather, pest, and disease alerts help reduce crop loss risk."
    },

    "real_time_monitoring_feature": {
        "keywords": ["real time monitoring", "फसल मॉनिटरिंग", "crop health check","health" ,"health monitoring feature"],
        "mr": "रिअल-टाइम उपग्रह आणि AI मॉनिटरिंगमुळे आरोग्य, ताण आणि कमतरता लवकर कळतात.",
        "hi": "रियल-टाइम मॉनिटरिंग से फसल स्वास्थ्य, तनाव और कमी जल्दी पहचान में आती है.",
        "en": "Real-time AI and satellite monitoring quickly detects stress, health issues, or deficiencies."
    },

    "soil_water_feature": {
        "keywords": ["soil moisture","water", "water stress", "soil map", "माती नकाशा", "irrigation decision"],
        "mr": "मातीतील ओलावा, पाण्याचा ताण आणि नकाशे मदतीने योग्य सिंचन निर्णय घेता येतात.",
        "hi": "मिट्टी की नमी, पानी तनाव और मैपिंग से सही सिंचाई निर्णय लिए जा सकते हैं.",
        "en": "Soil moisture, water stress and mapping help guide correct irrigation decisions."
    },

    "pest_disease_feature": {
        "keywords": ["pest alert","pest", "disease alert", "कीट रोग अलर्ट", "pest feature"],
        "mr": "AI कीड व रोगाचा धोका ओळखून आधीच अलर्ट पाठवतो.",
        "hi": "AI कीट और रोग का खतरा पहचानकर पहले ही अलर्ट भेजता है.",
        "en": "AI detects pest and disease risk early and sends alerts."
    },

    "weather_feature": {
        "keywords": ["weather forecast", "मौसम जानकारी", "weather", "rain prediction", "खेत मौसम"],
        "mr": "हवामान अंदाजामुळे पेरणी, फवारणी, सिंचन यांची योग्य वेळ निवडता येते.",
        "hi": "मौसम पूर्वानुमान से बुवाई, सिंचाई और स्प्रे का सही समय चुनना आसान होता है.",
        "en": "Weather forecasts help plan irrigation, spraying, and field operations efficiently."
    },
    # ... INCLUDE THE REST OF YOUR QNA_DATASET HERE ...
    "fallback_message": {
        "keywords": ["fallback_trigger"],
        "mr": "क्षमा करा, API काम करत नाहीये आणि या प्रश्नाचे उत्तर आमच्या QA ज्ञान आधारामध्ये उपलब्ध नाही. कृपया वेगळा प्रश्न विचारा.",
        "hi": "क्षमा करें, API काम नहीं कर रहा है और इस प्रश्न का उत्तर हमारे QA ज्ञान आधार में उपलब्ध नहीं है। कृपया कोई और प्रश्न पूछें।",
        "en": "The API is currently unavailable, and the answer to this specific question is not found in our QA Knowledge Base. Please ask a different question."
    }
}


def find_answer(query, lang):
    query = query.lower()

    for item in QA_DATASET.values():
        for k in item["keywords"]:
            if k.lower() in query:
                return item.get(lang, item["en"])

    return None

# -----------------------------
# PUBLIC API
# -----------------------------
class Query(BaseModel):
    query: str
    lang: str

@app.post("/public/query")
def public_query(payload: Query):
    answer = find_answer(payload.query, payload.lang)

    if answer:
        return {"answer": answer}

    return {"answer": "Feel free to contact us at \nsales@planeteyefarm.ai  \nContact : +91 8275830454.   \nPlanetEye Farm AI LtdCorporate office: Survey No.51, 3rd Floor, KK Plaza, Nashik(MH) India -422013"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8070, reload=True)
