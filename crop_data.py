"""
CropCare - Comprehensive Crop Information Center Data
Agricultural knowledge base containing detailed scientific, agronomical,
and pathological profiles for Rice, Tomato, Cotton, and Maize.
"""

CROPS = {
    "rice": {
        "id": "rice",
        "name": "Rice",
        "scientific_name": "Oryza sativa",
        "family": "Poaceae (Gramineae)",
        "icon": "🌾",
        "category": "Cereal Grain / Staple Food",
        "tagline": "The staple sustenance for more than half the world's population, thriving in warm, wetland agro-ecosystems.",
        "overview": (
            "Rice is the most widely consumed staple food for a large part of the human population, "
            "especially in Asia. It is a semiaquatic annual grass that thrives in water-abundant, "
            "warm tropical and subtropical climates. High yield requires careful nutrient balancing, "
            "controlled water inundation, and diligent disease management from nursery till panicle harvest."
        ),
        "growing_conditions": {
            "soil": "Heavy clayey loam or silty clay with high moisture-retention capacity; pH 5.5 – 7.0.",
            "temperature": "Warm & humid climate with optimal temperatures of 20°C to 35°C (germination >10°C, flowering 25°C–29°C).",
            "rainfall": "1000 – 1500 mm well-distributed; flooded or standing water (2–5 cm) required during vegetative growth stages.",
            "sunlight": "High solar radiation with 6 to 8 hours of direct daily sunlight for maximum tillering and grain filling.",
            "sowing_harvest": "Kharif (June–November), Rabi (November–April), and Summer/Boro cycles depending on water availability.",
            "spacing": "20 cm × 15 cm or 15 cm × 15 cm spacing for transplanted seedlings (2–3 seedlings per hill)."
        },
        "agronomic_tips": [
            "Maintain 2–3 cm shallow standing water during early tillering; drain field before nitrogen top-dressing.",
            "Apply zinc sulfate (25 kg/ha) at basal preparation to prevent Khaira disease (zinc deficiency).",
            "Perform seed treatment with Carbendazim (2 g/kg of seeds) 24 hours prior to nursery sowing."
        ],
        "diseases": [
            {
                "name": "Rice Blast",
                "pathogen": "Magnaporthe oryzae (Fungal)",
                "severity": "High",
                "symptoms": (
                    "Spindle-shaped or diamond lesions on leaves with grayish-white centers and dark reddish-brown borders. "
                    "Lesions enlarge and coalesce, blighting entire leaves. Neck blast causes blackening and rotting of panicle nodes, "
                    "leading to empty, chalky, or broken grain heads."
                ),
                "prevention": (
                    "Use certified blast-resistant varieties (e.g., IR64, MTU1010, Samba Mahsuri). "
                    "Avoid excessive split applications of chemical nitrogen fertilizers. "
                    "Maintain proper hill spacing to discourage dense humid microclimates."
                ),
                "treatment": (
                    "Treat seeds with Tricyclazole 75% WP @ 2 g/kg seed before sowing. "
                    "At first symptom appearance on leaves or boot leaf, spray Tricyclazole 75% WP @ 0.6 g/L or "
                    "Isoprothiolane 40% EC @ 1.5 ml/L of water. Repeat after 10–14 days if wet, misty conditions continue."
                )
            },
            {
                "name": "Bacterial Leaf Blight (BLB)",
                "pathogen": "Xanthomonas oryzae pv. oryzae (Bacterial)",
                "severity": "High",
                "symptoms": (
                    "Water-soaked translucent lesions starting from leaf tips and margins, expanding into elongated wavy "
                    "yellowish-white stripes with irregular borders. In early morning or humid conditions, tiny amber-colored "
                    "bacterial ooze droplets appear on leaf surfaces. Causes systemic seedling wilt ('Kresek')."
                ),
                "prevention": (
                    "Plant BLB-resistant cultivars. Avoid clipping leaf tips of seedlings during transplanting. "
                    "Balance nitrogen with adequate potassium fertilization. Drain stagnant water from fields for 3–4 days."
                ),
                "treatment": (
                    "Foliar spray with Copper Oxychloride 50% WP @ 2.5 g/L mixed with Streptocycline (plant antibiotic) "
                    "@ 0.1 g/L of water. Avoid overhead spraying or field-to-field irrigation flow from diseased plots."
                )
            },
            {
                "name": "Brown Spot",
                "pathogen": "Bipolaris oryzae (Fungal)",
                "severity": "Moderate to High",
                "symptoms": (
                    "Small, circular to oval dark brown spots (sesame seed shape) with yellow chlorotic halos scattered "
                    "across the entire leaf blade. Centers turn gray-brown in mature spots. Grain glumes become heavily speckled "
                    "with dark patches, causing poor milling quality."
                ),
                "prevention": (
                    "Correct soil nutrient stress, especially nitrogen, potassium, and silicon deficiencies. "
                    "Hot water seed soaking at 53°C–54°C for 10–12 minutes. Ensure deep plowing of past crop residues."
                ),
                "treatment": (
                    "Seed treatment with Mancozeb 75% WP @ 3 g/kg of seed. Spray Mancozeb @ 2 g/L or Propiconazole 25% EC "
                    "@ 1 ml/L of water at tillering and boot leaf emergence."
                )
            },
            {
                "name": "Sheath Blight",
                "pathogen": "Rhizoctonia solani (Fungal)",
                "severity": "Moderate",
                "symptoms": (
                    "Oval, greenish-gray water-soaked spots with dark brown margins developing on leaf sheaths just above the waterline. "
                    "Lesions spread upward along upper sheaths and leaves in an irregular snake-skin pattern, causing lodging and grain sterility."
                ),
                "prevention": (
                    "Maintain optimal plant spacing to avoid dense canopy humidity; keep field bunds free from weed hosts. "
                    "Apply recommended doses of potash fertilizer in two splits."
                ),
                "treatment": (
                    "Spray Validamycin 3% L @ 2.5 ml/L or Hexaconazole 5% EC @ 2 ml/L of water, directing the spray nozzle "
                    "strictly toward the lower plant base and water line."
                )
            }
        ]
    },
    "tomato": {
        "id": "tomato",
        "name": "Tomato",
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae (Nightshade)",
        "icon": "🍅",
        "category": "Solanaceous Fruit / Commercial Vegetable",
        "tagline": "Nutrient-dense, high-value commercial horticultural crop with high responsiveness to intensive care.",
        "overview": (
            "Tomato is one of the most popular, versatile, and high-value vegetables grown worldwide. "
            "It requires warm, sunny conditions, consistent root moisture, and proactive fungal and viral "
            "disease monitoring. Due to its tender foliage and susceptibility to Solanaceae pathogens, "
            "regular canopy inspection and trellising are vital for high market yields."
        ),
        "growing_conditions": {
            "soil": "Well-drained sandy loam to clay loam rich in organic compost; optimal pH 6.0 – 7.0.",
            "temperature": "Warm season crop; ideal day temperature 21°C – 28°C, night temperature 15°C – 20°C. Pollination suffers above 35°C.",
            "rainfall": "600 – 800 mm evenly distributed; drip irrigation preferred to keep foliage dry and prevent blossom-end rot.",
            "sunlight": "Full, unshaded sunlight (6 to 8+ hours daily) for sturdy vegetative stems and uniform fruit ripening.",
            "sowing_harvest": "Year-round in frost-free regions; major planting cycles: Autumn (Aug–Dec) and Spring-Summer (Jan–May).",
            "spacing": "60 cm × 45 cm for determinate varieties; 75 cm × 60 cm for staked indeterminate hybrids."
        },
        "agronomic_tips": [
            "Prune bottom 20–30 cm of sucker branches to prevent soil-borne pathogens from splashing onto lower leaves.",
            "Mulch soil around plants with clean organic straw or silver-black reflective plastic mulch.",
            "Supply calcium nitrate during early flowering to prevent physiological Blossom End Rot (BER)."
        ],
        "diseases": [
            {
                "name": "Early Blight",
                "pathogen": "Alternaria solani (Fungal)",
                "severity": "Moderate to High",
                "symptoms": (
                    "Dark brown to black necrotic spots exhibiting distinctive concentric rings ('target-board' pattern) "
                    "surrounded by yellow chlorotic halos. Starts on oldest lower leaves and progresses upward; severe cases "
                    "cause stem lesions (collar rot) and dark sunken leathery spots at fruit stem ends."
                ),
                "prevention": (
                    "Rotate fields away from Solanaceae crops (potato, eggplant, pepper) for at least 3 years. "
                    "Prune lower foliage and stake vines to keep leaves dry. Water strictly at the root zone via drip tape."
                ),
                "treatment": (
                    "Apply protective sprays of Chlorothalonil 75% WP @ 2 g/L or Mancozeb 75% WP @ 2.5 g/L every 7–10 days. "
                    "In active outbreaks, spray systemic Azoxystrobin 23% SC @ 1 ml/L or Difenoconazole 25% EC @ 0.5 ml/L."
                )
            },
            {
                "name": "Late Blight",
                "pathogen": "Phytophthora infestans (Oomycete)",
                "severity": "Extremely High (Rapid Defoliation)",
                "symptoms": (
                    "Large, irregular water-soaked pale-green to olive-brown greasy patches on leaves and petioles. "
                    "Under humid or morning-dew conditions, a delicate white fuzzy fungal-like growth appears beneath the leaf. "
                    "Fruit develops greasy, golden-brown leathery rot that ruins the harvest within days."
                ),
                "prevention": (
                    "Avoid overhead sprinkler irrigation. Space plants generously to ensure rapid drying after rain. "
                    "Immediately destroy and bury infected plant cull piles away from the field."
                ),
                "treatment": (
                    "Preventive application of Copper Oxychloride 50% WP @ 2.5 g/L. At first confirmation, apply systemic "
                    "Metalaxyl-M + Mancozeb (Ridomil Gold) @ 2.5 g/L or Cymoxanil + Mancozeb @ 2 g/L of water."
                )
            },
            {
                "name": "Bacterial Spot",
                "pathogen": "Xanthomonas campestris pv. vesicatoria (Bacterial)",
                "severity": "Moderate",
                "symptoms": (
                    "Numerous small (1–3 mm), dark brown, water-soaked angular spots on foliage with prominent yellow margins. "
                    "Leaves look blighted and defoliate prematurely, leaving green fruits exposed to sunscald. "
                    "Fruit surfaces show small, raised, black scab-like pustules."
                ),
                "prevention": (
                    "Use certified disease-free hot-water-treated seed. Sanitize pruning shears, stakes, and trellis twine. "
                    "Avoid touching or working inside damp crop foliage."
                ),
                "treatment": (
                    "Foliar spray with Copper Hydroxide @ 2 g/L tank-mixed with Mancozeb @ 2 g/L. The copper-mancozeb mix "
                    "releases active copper ions that control copper-tolerant bacterial strains."
                )
            },
            {
                "name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
                "pathogen": "Begomovirus (Whitefly-transmitted Viral)",
                "severity": "High (Stunting & Flower Drop)",
                "symptoms": (
                    "Severe upward cupping and curling of leaf margins, reduced leaflet size, pale yellowing (chlorosis) along "
                    "vein edges, and pronounced stunted, bushy plant architecture. Infected early plants drop blossoms and set no fruit."
                ),
                "prevention": (
                    "Install yellow sticky traps (25–30 traps/hectare) to monitor and catch whitefly vectors (Bemisia tabaci). "
                    "Use 40–50 mesh insect-proof netting in nurseries. Plant resistant hybrids with Ty-genes."
                ),
                "treatment": (
                    "No chemical cure exists for viral infection. Immediately rogue out and bag infected plants. "
                    "Manage whitefly vectors by spraying Imidacloprid 17.8% SL @ 0.3 ml/L or Neem oil (10,000 ppm) @ 3 ml/L."
                )
            }
        ]
    },
    "cotton": {
        "id": "cotton",
        "name": "Cotton",
        "scientific_name": "Gossypium hirsutum",
        "family": "Malvaceae (Mallow)",
        "icon": "🌱",
        "category": "Fiber / Cash Crop ('White Gold')",
        "tagline": "The premier global natural textile fiber requiring warm temperatures, sunlit canopies, and pest-disease watchfulness.",
        "overview": (
            "Cotton is one of the world's most critical agricultural commercial cash crops, providing "
            "natural fiber for textiles and seed oil for industrial and feed use. Grown primarily in semi-arid "
            "and black soil regions, cotton demands deep fertile land, adequate heat units, and careful "
            "protection against foliar leaf blights, wilt fungi, and vector-borne viral complexes."
        ),
        "growing_conditions": {
            "soil": "Deep, well-drained fertile black clay soils ('regur') or deep alluvial loams with pH 6.5 – 8.5; good water retention.",
            "temperature": "Warm, sunny climate; requires 21°C to 30°C for vegetative growth. Minimum 180–200 frost-free days.",
            "rainfall": "500 – 1000 mm; sensitive to water stagnation during seedling and square/boll formation stages.",
            "sunlight": "Abundant bright sunshine (6+ hours daily); continuous cloudy weather promotes square shed and disease.",
            "sowing_harvest": "Major Kharif crop; sown between April–May (North Zone) and June–July (Central & South Zones).",
            "spacing": "90 cm × 45 cm or 120 cm × 60 cm depending on hybrid vigor, soil fertility, and canopy habit."
        },
        "agronomic_tips": [
            "Perform acid delinting of seeds using commercial concentrated sulfuric acid (100 ml/kg seed) to kill seed-borne pathogens.",
            "Avoid excessive nitrogenous fertilization which induces lush succulent growth vulnerable to sucking pests.",
            "Practice deep summer plowing to expose resting fungal resting structures (sclerotia) to solar heat."
        ],
        "diseases": [
            {
                "name": "Bacterial Blight / Black Arm",
                "pathogen": "Xanthomonas citri pv. malvacearum (Bacterial)",
                "severity": "High",
                "symptoms": (
                    "Four distinct phases: Angular leaf spot (small, dark brown, vein-bound spots on undersides of leaves), "
                    "Black Arm (elongated, dark brown to black canker lesions on petioles and main stems causing snapping), "
                    "seedling blight, and boll rot with dark sunken spots staining lint."
                ),
                "prevention": (
                    "Acid delinting of planting seeds; plant resistant cotton varieties. "
                    "Deeply incorporate past cotton residues into the soil. Avoid flood irrigation across infected fields."
                ),
                "treatment": (
                    "Seed treatment with Streptocycline @ 100 ppm (1 g per 10 L water) for 2 hours. "
                    "Foliar spray with Copper Oxychloride 50% WP @ 2.5 g/L mixed with Streptocycline @ 0.1 g/L of water. "
                    "Repeat after 12–15 days if rainfall continues."
                )
            },
            {
                "name": "Fusarium Wilt",
                "pathogen": "Fusarium oxysporum f. sp. vasinfectum (Fungal)",
                "severity": "High",
                "symptoms": (
                    "Progressive yellowing and browning along leaf margins beginning on lower branches; leaves lose turgor, "
                    "wilt, and drop prematurely. Splitting the main taproot and lower stem reveals a diagnostic dark brown or "
                    "black continuous ring of vascular discoloration in xylem tissues."
                ),
                "prevention": (
                    "Cultivate wilt-resistant hybrids. Practice long crop rotation with non-hosts like sorghum, pearl millet, or maize. "
                    "Control root-knot nematodes which create root entry wounds for fungal hyphae."
                ),
                "treatment": (
                    "Seed dressing with Trichoderma viride bio-fungicide @ 10 g/kg seed or Carbendazim 50% WP @ 2 g/kg seed. "
                    "Spot-drench infected root areas with Carbendazim @ 1 g/L or Benomyl @ 1 g/L of water."
                )
            },
            {
                "name": "Cotton Leaf Curl Virus (CLCuV)",
                "pathogen": "Begomovirus (Whitefly-transmitted Viral)",
                "severity": "High (Stunting & Crop Loss)",
                "symptoms": (
                    "Upward or downward curling of leaf margins, vein thickening on the undersurface of leaves, "
                    "and characteristic cup-shaped leaf-like enations protruding from the veins under leaves. "
                    "Plants are stunted, internodes shorten, and boll setting is drastically curtailed."
                ),
                "prevention": (
                    "Sow CLCuV-tolerant hybrids early in the season. Eradicate alternate weed hosts (Kanghi, Peeli Buti, Parthenium) "
                    "along field borders. Establish yellow sticky boards (20–25/acre)."
                ),
                "treatment": (
                    "Chemicals cannot cure viral infection. Rogue out and destroy early affected plants. "
                    "Suppress the whitefly vector using Diafenthiuron 50% WP @ 1.2 g/L or Acetamiprid 20% SP @ 0.2 g/L or "
                    "Pyriproxyfen 10% EC @ 1.5 ml/L of water."
                )
            },
            {
                "name": "Root Rot",
                "pathogen": "Rhizoctonia solani / Macrophomina phaseolina (Fungal)",
                "severity": "Moderate to High",
                "symptoms": (
                    "Sudden wilting and complete collapse of standing cotton plants in scattered patches. "
                    "Affected plants pull out easily from the ground; roots show shredded, rotted cortical bark "
                    "with dark pinhead-sized resting bodies (sclerotia) underneath."
                ),
                "prevention": (
                    "Intercrop cotton with moth bean or cluster bean to lower topsoil temperature. "
                    "Apply well-decomposed farmyard manure enriched with Trichoderma harzianum (2.5 kg/ha)."
                ),
                "treatment": (
                    "Seed treatment with Carboxin 37.5% + Thiram 37.5% DS @ 3 g/kg seed. "
                    "Drench root zones of neighboring plants in affected patches with Copper Oxychloride @ 3 g/L or "
                    "Carbendazim @ 1 g/L of water."
                )
            }
        ]
    },
    "maize": {
        "id": "maize",
        "name": "Maize (Corn)",
        "scientific_name": "Zea mays",
        "family": "Poaceae (Gramineae)",
        "icon": "🌽",
        "category": "Cereal Grain / C4 Wonder Crop",
        "tagline": "The 'Queen of Cereals' with exceptional photosynthetic efficiency and diverse food, feed, and industrial uses.",
        "overview": (
            "Maize (corn) is among the most versatile agricultural crops in the world, serving as staple food, "
            "animal feed, and industrial raw material (starch, ethanol, syrup). As a C4 physiological plant, "
            "maize converts sunlight and nutrients efficiently into biomass. Optimizing yield requires "
            "deep moisture during tasseling and silking, balanced nitrogen, and vigilant control against "
            "foliar blights and rusts."
        ),
        "growing_conditions": {
            "soil": "Deep, fertile, well-drained sandy loam to silty clay loam rich in organic matter; pH 5.8 – 7.5; zero tolerance to water stagnation.",
            "temperature": "Warm season crop; optimal temperatures range from 21°C to 32°C. Seed germination drops sharply below 13°C.",
            "rainfall": "500 – 800 mm evenly distributed; critical water stages are tasseling, silking, and early dough.",
            "sunlight": "Full direct sunlight (minimum 6–8 hours daily) for high photosynthetic output and cob development.",
            "sowing_harvest": "Cultivated across Kharif (June–October), Rabi (October–March), and Spring-Summer seasons.",
            "spacing": "60 cm × 20 cm or 75 cm × 20 cm (one plant per hill) ensuring 65,000–75,000 plants per hectare."
        },
        "agronomic_tips": [
            "Ensure ridge and furrow planting to avoid water stagnation at seedling stage, which induces damping-off.",
            "Apply nitrogen in 3 split doses: 1/3 at basal, 1/3 at knee-high stage (V6), and 1/3 at tasseling stage.",
            "Apply zinc sulfate (20–25 kg/ha) at field preparation to prevent white bud physiological disorder."
        ],
        "diseases": [
            {
                "name": "Northern Corn Leaf Blight (NCLB)",
                "pathogen": "Exserohilum turcicum (Fungal)",
                "severity": "High",
                "symptoms": (
                    "Long, elliptical, grayish-green or tan cigar-shaped necrotic lesions (2.5 to 15 cm long) on leaves. "
                    "Lesions develop dark olive-brown velvety fungal spores in damp weather and merge together, "
                    "giving the foliage a scorched, burnt appearance that curtails grain fill."
                ),
                "prevention": (
                    "Plant NCLB-resistant hybrid corn seeds. Rotate fields for 1–2 seasons with non-hosts like soybean or pulses. "
                    "Deeply plow under post-harvest stubble to reduce overwintering spore reservoirs."
                ),
                "treatment": (
                    "At first symptom detection (before tasseling), spray Mancozeb 75% WP @ 2.5 g/L or "
                    "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1 ml/L of water. Repeat spray at 14-day intervals if cool, humid weather persists."
                )
            },
            {
                "name": "Gray Leaf Spot (GLS)",
                "pathogen": "Cercospora zeae-maydis (Fungal)",
                "severity": "Moderate to High",
                "symptoms": (
                    "Small, tan or gray rectangular lesions strictly bounded by leaf veins that run parallel along the leaf blade, "
                    "creating a distinctive 'windowpane' pattern when held up to sunlight. Lesions merge to bluster broad sections of leaf tissue."
                ),
                "prevention": (
                    "Practice 2-year crop rotation; avoid continuous corn cropping. "
                    "Plant resistant or tolerant commercial hybrids; maintain balanced potash fertilization."
                ),
                "treatment": (
                    "Foliar spray with Propiconazole 25% EC @ 1 ml/L or Pyraclostrobin 20% WG @ 1 g/L of water "
                    "at tasseling or early silking stage if disease pressure is noted."
                )
            },
            {
                "name": "Common Rust",
                "pathogen": "Puccinia sorghi (Fungal)",
                "severity": "Moderate",
                "symptoms": (
                    "Small, circular to elongate, powdery cinnamon-brown to golden pustules scattered densely on both upper and "
                    "lower leaf surfaces. As pustules mature, leaf epidermis ruptures and powdery spores rub off easily. "
                    "Late in the season, pustules turn brownish-black."
                ),
                "prevention": (
                    "Grow rust-resistant hybrid varieties. Plant early in the season to escape peak late-season airborne spore showers. "
                    "Avoid over-application of nitrogen fertilizer."
                ),
                "treatment": (
                    "Apply foliar spray of Chlorothalonil 75% WP @ 2 g/L or Mancozeb @ 2.5 g/L or Tebuconazole 25.9% EC "
                    "@ 1 ml/L of water if pustules appear on upper leaves before silking."
                )
            },
            {
                "name": "Bacterial Stalk Rot",
                "pathogen": "Dickeya zeae (Bacterial)",
                "severity": "High (Stalk Lodging)",
                "symptoms": (
                    "Water-soaked dark lesions on lower internodes near ground level; stems become soft, spongy, and waterlogged, "
                    "emitting a foul, putrid odor. Upper leaves wilt rapidly while remaining dull green; stalks collapse and lodge easily."
                ),
                "prevention": (
                    "Provide prompt furrow drainage; avoid using stagnant drainage water for irrigation. "
                    "Avoid excessive plant population that traps humidity around lower stems."
                ),
                "treatment": (
                    "Bleaching powder (Chlorine 33%) drenching along rows @ 10–12 kg/ha. "
                    "Foliar and collar spray with Copper Oxychloride 50% WP @ 3 g/L mixed with Streptocycline @ 0.15 g/L."
                )
            }
        ]
    }
}


def get_all_crops():
    """Return all crop profiles as a dictionary."""
    return CROPS


def get_crop_list():
    """Return a list of all crop objects for easy iteration."""
    return list(CROPS.values())


def get_crop_by_id(crop_id):
    """Retrieve a single crop profile by its ID (e.g., 'rice', 'tomato', 'cotton', 'maize')."""
    if not crop_id:
        return None
    return CROPS.get(crop_id.lower().strip())
