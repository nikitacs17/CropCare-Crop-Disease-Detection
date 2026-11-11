import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'crop_disease_model.onnx')

# PlantVillage 38-Class Agricultural Knowledge Base
DISEASE_KNOWLEDGE_BASE = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "is_healthy": False,
        "symptoms": "Dull olive-green to brown velvety spots on the upper leaf surface, yellowing foliage, and premature leaf drop.",
        "treatment": "Rake and destroy fallen leaves to reduce overwintering fungi. Apply preventive bio-fungicides or copper/captan-based sprays during early bud break."
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot",
        "is_healthy": False,
        "symptoms": "Purple flecks on leaves that enlarge into circular 'frog-eye' leaf spots with light centers and dark borders. Rotten fruit turns into black mummies.",
        "treatment": "Prune infected cankers and dead wood during dormant season. Remove mummified fruit from trees and ground. Apply copper or sulfur fungicides."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "is_healthy": False,
        "symptoms": "Bright yellow-orange spots on upper leaf surfaces that develop tiny raised black specks; tubular structures form beneath the leaf.",
        "treatment": "Remove nearby eastern red cedar trees if practical. Apply protective fungicides like myclobutanil or mancozeb at pink bud stage."
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Foliage shows vibrant green color, strong leaf veins, and smooth leaf margins with no active fungal lesions or pest damage.",
        "treatment": "Maintain balanced nitrogen fertilization, regular watering, and good sunlight exposure to sustain natural plant immunity."
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Leaves are crisp, glossy dark green, and free from chlorosis or fungal spots.",
        "treatment": "Maintain soil pH around 4.5–5.2, apply organic pine bark mulch, and irrigate with clean, non-alkaline water."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "symptoms": "White to grayish powdery fungal growth on leaves and shoots, causing leaf curling, upward cupping, and stunted shoot growth.",
        "treatment": "Improve air circulation through canopy pruning. Spray potassium bicarbonate, neem oil, or sulfur-based fungicides when symptoms appear."
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Uniform rich green leaves with healthy serrated edges and vigorous branch growth.",
        "treatment": "Ensure adequate deep watering during fruit development and apply balanced organic compost in early spring."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "is_healthy": False,
        "symptoms": "Narrow, rectangular tan or gray lesions restricted by leaf veins that run parallel along the leaves.",
        "treatment": "Practice crop rotation with non-host crops (soybean/pulses). Plow under crop residues and plant resistant hybrid corn varieties."
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "is_healthy": False,
        "symptoms": "Small, powdery cinnamon-brown to golden pustules scattered on both upper and lower leaf surfaces.",
        "treatment": "Plant rust-resistant hybrids. In severe cases, apply strobilurin or triazole fungicides at the first sign of pustules."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "is_healthy": False,
        "symptoms": "Long, elliptical grayish-green or tan cigar-shaped lesions measuring 1 to 6 inches long across leaves.",
        "treatment": "Rotate crops every two seasons, till residue into the soil, and use resistant seed hybrids with foliar fungicide if needed."
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Broad, upright green leaves free from chlorosis, rust pustules, or striping.",
        "treatment": "Maintain proper nitrogen and zinc fertilization and ensure sufficient moisture during the silking stage."
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "is_healthy": False,
        "symptoms": "Small reddish-brown circular spots on leaves surrounded by dark margins. Berries turn brown, shrivel, and dry into black wrinkled mummies.",
        "treatment": "Prune dead canes and destroy mummified berries. Apply copper hydroxide or mancozeb sprays starting from early shoot growth until veraison."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "is_healthy": False,
        "symptoms": "'Tiger-stripe' chlorotic patterns with necrotic centers between main veins; small dark spots on berry skins.",
        "treatment": "Protect pruning wounds with wound sealants or paste. Prune during dry weather and remove severely infected trunks to protect the vineyard."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight",
        "is_healthy": False,
        "symptoms": "Irregular dark brown or black angular leaf spots that coalesce, causing premature leaf drying and leaf drop.",
        "treatment": "Prune lower vine canopy to improve airflow and reduce humidity. Spray copper-based fungicides after seasonal rains."
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Vibrant, broad green lobed leaves with clean margins and no fungal discoloration or webbing.",
        "treatment": "Maintain proper trellising, balanced potassium-phosphorus fertilization, and adequate drip irrigation."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange (Citrus)",
        "disease": "Citrus Greening (Huanglongbing)",
        "is_healthy": False,
        "symptoms": "Asymmetrical blotchy yellow mottle on leaves, yellowing veins, upright stunted leaves, and small misshapen bitter fruit.",
        "treatment": "Control the Asian citrus psyllid vector with systemic insecticidal treatments. Remove and safely destroy confirmed infected trees."
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": "Small angular water-soaked spots on leaves that turn reddish-brown and fall out, giving leaves a 'shot-hole' appearance.",
        "treatment": "Apply copper sprays during dormant season and oxytetracycline sprays during bloom. Avoid excessive nitrogen fertilizing."
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Long, lance-shaped shiny green leaves without lesions, holes, or curled edges.",
        "treatment": "Thin fruit properly, apply winter dormant oil, and provide adequate water during summer fruit development."
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": "Small, water-soaked yellowish-green blister spots on lower leaves that turn dark brown and cause extensive defoliation.",
        "treatment": "Use certified disease-free seeds. Avoid overhead sprinkler irrigation. Spray fixed copper combined with mancozeb as a protective spray."
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Smooth, dark green foliage with healthy branching and active flower buds.",
        "treatment": "Maintain warm soil temperatures, apply balanced calcium-rich fertilizers, and mulch with straw to retain soil moisture."
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "is_healthy": False,
        "symptoms": "Dark brown to black spots with characteristic concentric rings ('target board' pattern) appearing first on older lower leaves.",
        "treatment": "Practice a 3-year crop rotation. Space plants to promote drying. Apply chlorothalonil or copper-based protective sprays upon first signs."
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "is_healthy": False,
        "symptoms": "Large, irregular water-soaked dark lesions on leaf tips with white cottony fungal mold under leaves in moist weather.",
        "treatment": "Destroy infected volunteer tubers. Apply systemic fungicides like metalaxyl or mancozeb before humid rainy spells. Ensure high hilling."
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Dense, uniform green foliage with robust compound leaves and no necrotic spotting.",
        "treatment": "Hill plants consistently to protect tubers, ensure deep drainage, and test soil nutrient balance annually."
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Vigorous serrated trifoliate green leaves with no cane blight or rust markings.",
        "treatment": "Prune spent floricanes after fruiting, maintain adequate row spacing for ventilation, and weed regularly."
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Deep green trifoliate leaves with clean surfaces and strong nodulating roots.",
        "treatment": "Rotate crops with grains, maintain proper soil phosphorus, and scout early for pest infestations."
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "symptoms": "Talc-like white circular fungal powdery patches on leaf surfaces, stems, and petioles; leaves yellow, dry, and die.",
        "treatment": "Spray horticultural neem oil or diluted potassium bicarbonate solution. Water the soil base rather than foliage."
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "is_healthy": False,
        "symptoms": "Numerous small, irregular purple to dark brown blotches covering leaves; leaf margins curl upward and appear scorched or burned.",
        "treatment": "Remove old infected leaves after harvest. Avoid overhead sprinkler irrigation. Apply captan or copper fungicides in early spring."
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Bright emerald green trifoliate leaves with serrated margins and healthy flower trusses.",
        "treatment": "Mulch beds with clean straw to keep leaves away from wet soil, and fertilize lightly with organic nitrogen."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "symptoms": "Small, dark greasy spots with yellow halos on leaves; leaves turn yellow and drop prematurely.",
        "treatment": "Sanitize stakes and tools. Water at the plant base with drip lines. Spray copper fungicide mixed with mancozeb weekly during wet periods."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "is_healthy": False,
        "symptoms": "Concentric ringed brown lesions surrounded by yellow halos starting from lower older leaves and moving upward.",
        "treatment": "Prune bottom 12 inches of foliage to stop soil splashing. Mulch around stems and apply copper or chlorothalonil fungicides."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "is_healthy": False,
        "symptoms": "Large, irregular greasy olive-brown to black patches on leaves and stems; white fuzzy fungal growth appears under leaves in damp weather.",
        "treatment": "Immediately remove and dispose of infected plants. Do not compost. Apply protective copper sprays to unaffected plants in cool wet weather."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "is_healthy": False,
        "symptoms": "Pale green or yellowish spots on upper leaf surfaces, with an olive-green to brownish velvety mold growth directly underneath.",
        "treatment": "Improve greenhouse or garden airflow by increasing plant spacing. Keep relative humidity below 85% and spray sulfur if required."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "is_healthy": False,
        "symptoms": "Many small circular spots (1-3mm) with light gray or tan centers and dark brown margins; tiny black speck pycnidia in center.",
        "treatment": "Avoid overhead watering. Cleanly prune infected lower foliage. Apply fungicides containing copper or chlorothalonil."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Spider Mites (Two-Spotted Spider Mite)",
        "is_healthy": False,
        "symptoms": "Fine yellow stippling or specks across leaf surfaces; dense fine silk webbing on undersides of leaves; leaves become bronze and brittle.",
        "treatment": "Spray underside of leaves with horticultural soap, neem oil, or insecticidal oil. Introduce predatory mites (Phytoseiulus persimilis)."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "is_healthy": False,
        "symptoms": "Small, water-soaked brown lesions with concentric circles that expand, causing extensive leaf yellowing and blighting.",
        "treatment": "Ensure good plant spacing and stake plants off the ground. Apply preventive azoxystrobin or copper-based sprays."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "symptoms": "Severe upward leaf cupping, reduced leaf size, mottled yellow leaf margins, and stunted, bushy plant growth with flower drop.",
        "treatment": "Control whitefly vectors using yellow sticky traps and insecticidal soaps. Use silver reflective mulches and plant TYLCV-resistant varieties."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "symptoms": "Mottled light and dark green mosaic patterns on leaves, distortion ('shoestringing'), and blistered appearance.",
        "treatment": "Wash hands and disinfect garden tools with 20% non-fat dry milk solution. Remove infected plants promptly; control aphids."
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy Leaf",
        "is_healthy": True,
        "symptoms": "Deep green foliage with robust compound leaflets, vigorous stem growth, and no discoloration or spotting.",
        "treatment": "Ensure steady deep watering, mulch soil, provide balanced organic fertilizer, and support with sturdy cages or stakes."
    }
}

# Ordered class names matching benchmark PlantVillage dataset
CLASS_NAMES = list(DISEASE_KNOWLEDGE_BASE.keys())


def check_ml_environment():
    """
    Check if the required machine learning libraries and model file are present.
    Returns: (is_ready: bool, status_message: str)
    """
    try:
        import numpy
        import PIL
        import onnxruntime
    except ImportError as e:
        missing_module = str(e).split("'")[-2] if "'" in str(e) else str(e)
        return False, f"ML package '{missing_module}' is not installed in the Python environment."

    if not os.path.exists(MODEL_PATH):
        return False, f"Trained ONNX model file not found at 'models/crop_disease_model.onnx'."

    return True, "ML environment and model file are ready."


def predict_disease(image_path):
    """
    Preprocess image and execute inference using the trained ONNX model.
    image_path: Absolute or relative path to the uploaded crop leaf image.
    
    Returns: dict with diagnostic outcome:
      - status: 'success', 'pending_model', or 'unreliable'
      - crop_name
      - disease_name
      - confidence
      - is_healthy
      - symptoms
      - treatment
      - message
    """
    is_ready, env_message = check_ml_environment()

    # If the user has not yet installed onnxruntime or downloaded the model weights,
    # we return a clean 'pending_model' status with clear setup steps.
    # We DO NOT produce fake random predictions.
    if not is_ready:
        return {
            "status": "pending_model",
            "crop_name": "Pending Model Setup",
            "disease_name": "Model Integration Required",
            "confidence": 0.0,
            "is_healthy": False,
            "symptoms": "AI model inference is pending library and weights setup.",
            "treatment": "Please install the ML libraries (pip install onnxruntime pillow numpy) and place 'crop_disease_model.onnx' in the models/ folder.",
            "message": env_message
        }

    try:
        import numpy as np
        from PIL import Image
        import onnxruntime as ort

        # 1. Load and convert image to RGB
        img = Image.open(image_path).convert('RGB')

        # 2. Resize to model standard input (224x224)
        img = img.resize((224, 224), Image.Resampling.BILINEAR)

        # 3. Convert to numpy array and normalize to [0, 1]
        img_array = np.array(img, dtype=np.float32) / 255.0

        # 4. Normalization matching model preprocessor_config.json (MobileNetV2 [0.5, 0.5, 0.5])
        mean = np.array([0.5, 0.5, 0.5], dtype=np.float32)
        std = np.array([0.5, 0.5, 0.5], dtype=np.float32)
        img_array = (img_array - mean) / std

        # 5. Reshape from (H, W, C) to (1, C, H, W) for PyTorch/ONNX standard
        img_array = np.transpose(img_array, (2, 0, 1))
        input_tensor = np.expand_dims(img_array, axis=0)

        # 6. Initialize ONNX Runtime session and run inference
        session = ort.InferenceSession(MODEL_PATH, providers=['CPUExecutionProvider'])
        input_name = session.get_inputs()[0].name
        outputs = session.run(None, {input_name: input_tensor})
        logits = outputs[0][0]

        # 7. Compute Softmax probabilities
        exp_logits = np.exp(logits - np.max(logits))
        probabilities = exp_logits / np.sum(exp_logits)

        # 8. Extract top predicted class and confidence score
        pred_idx = int(np.argmax(probabilities))
        confidence = float(probabilities[pred_idx]) * 100.0
        predicted_raw_class = CLASS_NAMES[pred_idx] if pred_idx < len(CLASS_NAMES) else None

        if not predicted_raw_class or predicted_raw_class not in DISEASE_KNOWLEDGE_BASE:
            return {
                "status": "unreliable",
                "crop_name": "Unknown",
                "disease_name": "Unrecognized Crop / Leaf",
                "confidence": round(confidence, 1),
                "is_healthy": False,
                "symptoms": "The uploaded image could not be matched with high certainty to any supported crop leaf.",
                "treatment": "Please capture a clear, well-lit photograph focusing on a single leaf of a supported crop.",
                "message": "Diagnosis unreliable due to unrecognized features."
            }

        # 9. Low confidence threshold (< 45%): Mark as unreliable instead of misleading the farmer
        if confidence < 45.0:
            return {
                "status": "unreliable",
                "crop_name": "Uncertain",
                "disease_name": "Unreliable Prediction (Low Confidence)",
                "confidence": round(confidence, 1),
                "is_healthy": False,
                "symptoms": f"The model detected weak symptoms ({round(confidence, 1)}% confidence), which is too low to guarantee an accurate diagnosis.",
                "treatment": "Ensure the leaf fills the camera view, avoid shadows or extreme glare, and verify that the crop is supported.",
                "message": "Low confidence score. Please upload a clearer leaf picture."
            }

        # 10. Successful reliable diagnosis
        info = DISEASE_KNOWLEDGE_BASE[predicted_raw_class]
        return {
            "status": "success",
            "crop_name": info["crop"],
            "disease_name": info["disease"],
            "confidence": round(confidence, 1),
            "is_healthy": info["is_healthy"],
            "symptoms": info["symptoms"],
            "treatment": info["treatment"],
            "message": "Diagnosis completed successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "crop_name": "Error",
            "disease_name": "Inference Error",
            "confidence": 0.0,
            "is_healthy": False,
            "symptoms": "An unexpected error occurred during image processing.",
            "treatment": "Please check the image file integrity or restart the web application.",
            "message": str(e)
        }
