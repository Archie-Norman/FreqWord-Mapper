topic_dict = {
    'unkown': [],  # Default category (empty list means all words not in other categories)
    
    'business': ['account', 'acquisition', 'advertisement', 'assets', 'audit', 
                'bankruptcy', 'board', 'brand', 'broker', 'capital', 'ceo', 'cfo',
                'commerce', 'commodity', 'competitor', 'consumer', 'contract', 'corporation',
                'cost', 'credit', 'currency', 'customer', 'debt', 'dividend', 'economics',
                'enterprise', 'entrepreneur', 'equity', 'export', 'finance', 'fiscal',
                'franchise', 'fund', 'goods', 'gross', 'import', 'income', 'industry',
                'inflation', 'interest', 'inventory', 'investment', 'invoice', 'leadership',
                'liability', 'liquidity', 'loan', 'logistics', 'management', 'market',
                'merger', 'monopoly', 'mortgage', 'negotiation', 'net', 'operating',
                'outsourcing', 'overhead', 'partnership', 'patent', 'payroll', 'portfolio',
                'premium', 'product', 'profit', 'quotation', 'receipt', 'recession',
                'recruitment', 'revenue', 'salary', 'shareholder', 'stock', 'subsidiary',
                'supply', 'tariff', 'tax', 'trade', 'transaction', 'turnover', 'venture',
                'wholesale', 'yield', 'startup', 'valuation', 'roi', 'kpi', 'benchmark',
                'cashflow', 'break-even', 'stakeholder', 'merchandise', 'endorsement'],
    
    'science': ['acceleration', 'acid', 'alkali', 'alloy', 'anatomy', 'astronomy', 'atom',
               'bacteria', 'biochemistry', 'biology', 'botany', 'cell', 'chemical',
               'chemistry', 'climate', 'compound', 'condensation', 'conduction', 'density',
               'dna', 'earthquake', 'ecology', 'electron', 'element', 'energy', 'enzyme',
               'evolution', 'experiment', 'fission', 'force', 'friction', 'fusion', 'gene',
               'genetics', 'gravity', 'habitat', 'hypothesis', 'laboratory', 'magnetism',
               'mass', 'matter', 'microscope', 'mineral', 'molecule', 'neutron', 'nucleus',
               'organism', 'oxidation', 'particle', 'photosynthesis', 'physics', 'proton',
               'radiation', 'reaction', 'resistance', 'solution', 'species', 'spectrum',
               'temperature', 'theory', 'thermodynamics', 'velocity', 'virus', 'volume',
               'wavelength', 'zoology', 'petri', 'quantum', 'relativity', 'paleontology',
               'neuroscience', 'biome', 'isotope', 'catalyst', 'polymer', 'nanotechnology'],
    
    'technology': ['algorithm', 'app', 'application', 'artificial', 'automation', 'bandwidth',
                  'binary', 'browser', 'cache', 'cloud', 'code', 'compiler', 'computation',
                  'computer', 'database', 'debug', 'digital', 'encryption', 'firewall',
                  'firmware', 'framework', 'gadget', 'hardware', 'interface', 'internet',
                  'iteration', 'kernel', 'machine', 'malware', 'network', 'node', 'open',
                  'platform', 'processor', 'program', 'protocol', 'query', 'script',
                  'server', 'software', 'storage', 'syntax', 'system', 'update', 'user',
                  'virtual', 'virus', 'website', 'blockchain', 'cryptography', 'cybersecurity',
                  'metadata', 'api', 'devops', 'iot', 'machine-learning', 'neural-network',
                  'robotics', 'sdk', 'ui', 'ux', 'vr', 'ar', 'big-data', 'data-mining'],
    
    'health': ['allergy', 'ambulance', 'anatomy', 'antibiotic', 'appointment', 'bacteria',
              'blood', 'bone', 'cancer', 'cardiac', 'clinic', 'diagnosis', 'diet',
              'disease', 'disorder', 'doctor', 'dose', 'emergency', 'exercise',
              'fever', 'fracture', 'gene', 'genetic', 'health', 'hospital', 'immune',
              'infection', 'injury', 'insurance', 'intensive', 'laboratory', 'medical',
              'medicine', 'nurse', 'nutrition', 'operation', 'organ', 'pain', 'patient',
              'pharmacy', 'physical', 'prescription', 'prevention', 'recovery',
              'rehabilitation', 'research', 'respiratory', 'screening', 'sickness',
              'surgery', 'symptom', 'therapy', 'treatment', 'vaccine', 'virus',
              'vitamin', 'ward', 'xray', 'pediatric', 'oncology', 'psychiatry', 'dental',
              'optometry', 'epidemic', 'pandemic', 'hygiene', 'wellness', 'obesity'],
    
    'legal': ['affidavit', 'appeal', 'arbitration', 'arrest', 'attorney', 'bail',
             'bankruptcy', 'bias', 'brief', 'case', 'civil', 'clause', 'client',
             'complaint', 'constitution', 'contract', 'copyright', 'court', 'crime',
             'damages', 'defendant', 'deposition', 'discovery', 'dismissal', 'dispute',
             'divorce', 'document', 'enforcement', 'evidence', 'felony', 'fraud',
             'hearing', 'immunity', 'indictment', 'injunction', 'judge', 'judgment',
             'jury', 'justice', 'law', 'lawsuit', 'lawyer', 'legal', 'legislation',
             'liability', 'license', 'litigation', 'misdemeanor', 'motion', 'negligence',
             'notary', 'oath', 'objection', 'opinion', 'parole', 'patent', 'penalty',
             'plaintiff', 'plea', 'precedent', 'probation', 'prosecution', 'record',
             'ruling', 'sentence', 'settlement', 'statute', 'subpoena', 'summons',
             'testimony', 'tort', 'trial', 'verdict', 'violation', 'warrant', 'witness',
             'jurisdiction', 'defamation', 'embezzlement', 'homicide', 'injunction',
             'libel', 'perjury', 'subrogation', 'trademark'],
    
    'education': ['academic', 'admission', 'algebra', 'assignment', 'attendance', 'bachelor',
                 'biology', 'blackboard', 'campus', 'chemistry', 'class', 'classroom',
                 'college', 'course', 'credit', 'curriculum', 'degree', 'diploma',
                 'discipline', 'dissertation', 'dormitory', 'education', 'elementary',
                 'essay', 'exam', 'faculty', 'grade', 'graduate', 'history', 'homework',
                 'institute', 'instruction', 'knowledge', 'language', 'lecture', 'lesson',
                 'literature', 'major', 'mathematics', 'middle', 'notebook', 'paper',
                 'philosophy', 'physics', 'principal', 'professor', 'program', 'project',
                 'promotion', 'reading', 'reference', 'research', 'school', 'science',
                 'semester', 'seminar', 'student', 'study', 'subject', 'teacher', 'teaching',
                 'test', 'textbook', 'thesis', 'training', 'tuition', 'university', 'writing',
                 'kindergarten', 'preschool', 'scholarship', 'syllabus', 'workshop', 'tutor',
                 'plagiarism', 'valedictorian', 'extracurricular', 'tenure', 'pedagogy'],
    
    # New categories added below
    'arts': ['painting', 'sculpture', 'music', 'dance', 'theater', 'opera', 'ballet',
             'photography', 'film', 'literature', 'poetry', 'novel', 'sketch', 'canvas',
             'exhibition', 'gallery', 'museum', 'aesthetic', 'portrait', 'landscape',
             'abstract', 'impressionism', 'symphony', 'jazz', 'folk', 'ceramics',
             'calligraphy', 'architecture', 'cinematography', 'choreography', 'mural',
             'watercolor', 'printmaking', 'avant-garde', 'performance', 'illustration'],
    
    'sports': ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
              'swimming', 'athletics', 'olympics', 'marathon', 'cricket', 'rugby',
              'volleyball', 'hockey', 'boxing', 'wrestling', 'badminton', 'cycling',
              'gymnastics', 'surfing', 'skiing', 'snowboarding', 'fencing', 'archery',
              'coach', 'referee', 'tournament', 'championship', 'stadium', 'arena',
              'penalty', 'dribble', 'home-run', 'ace', 'par', 'tackle', 'defense',
              'offense', 'goalkeeper', 'pitcher', 'racket', 'puck', 'medal', 'trophy'],
    
    'food': ['restaurant', 'cuisine', 'recipe', 'ingredient', 'chef', 'menu',
            'appetizer', 'entree', 'dessert', 'beverage', 'vegetarian', 'vegan',
            'gluten-free', 'organic', 'spice', 'herb', 'sauce', 'marinade',
            'baking', 'grilling', 'sauteing', 'frying', 'steaming', 'roasting',
            'sushi', 'pasta', 'pizza', 'burger', 'salad', 'soup', 'curry',
            'barbecue', 'pastry', 'bakery', 'butcher', 'dairy', 'produce',
            'gourmet', 'fusion', 'microwave', 'cutlery', 'napkin', 'leftovers'],
    
    'travel': ['airport', 'airline', 'luggage', 'passport', 'visa', 'itinerary',
              'destination', 'accommodation', 'hotel', 'hostel', 'resort', 'cruise',
              'sightseeing', 'tourist', 'backpacking', 'souvenir', 'currency',
              'exchange', 'boarding', 'departure', 'arrival', 'customs', 'immigration',
              'guidebook', 'landmark', 'adventure', 'excursion', 'expedition',
              'hiking', 'camping', 'safari', 'vacation', 'getaway', 'jetlag',
              'itinerary', 'amenities', 'check-in', 'check-out', 'layover', 'nonstop'],
    
    'environment': ['recycling', 'conservation', 'pollution', 'deforestation', 'sustainability',
                   'ecosystem', 'biodiversity', 'climate-change', 'global-warming', 'carbon',
                   'emissions', 'renewable', 'solar', 'wind', 'hydro', 'geothermal', 'compost',
                   'endangered', 'extinction', 'habitat', 'preservation', 'organic', 'greenhouse',
                   'ozone', 'watershed', 'erosion', 'contamination', 'landfill', 'biodegradable',
                   'footprint', 'ecology', 'reforestation', 'conservation', 'wildlife', 'sanctuary'],
    
    'politics': ['democracy', 'republic', 'monarchy', 'socialism', 'communism', 'capitalism',
                'federalism', 'nationalism', 'liberalism', 'conservatism', 'election',
                'campaign', 'candidate', 'vote', 'referendum', 'ballot', 'inauguration',
                'diplomacy', 'treaty', 'sanctions', 'embassy', 'ambassador', 'summit',
                'parliament', 'congress', 'senate', 'legislature', 'bill', 'veto',
                'impeachment', 'coalition', 'lobbyist', 'bureaucracy', 'sovereignty',
                'autonomy', 'geopolitics', 'ideology', 'propaganda', 'gerrymandering'],

    'finance': ['interest', 'inflation', 'stocks', 'bonds', 'dividend', 'portfolio', 'hedge', 
               'derivative', 'cryptocurrency', 'bitcoin', 'ethereum', 'blockchain', 'fiat',
               'forex', 'liquidity', 'recession', 'bull-market', 'bear-market', 'ipo', 'roi',
               'mutual-fund', 'etf', 'credit-score', 'loan', 'mortgage', 'refinance', 'audit',
               'taxation', 'capital-gains', 'compound-interest', 'annuity', 'pension', '401k',
               'insider-trading', 'volatility', 'diversification', 'leverage', 'short-selling',
               'market-cap', 'blue-chip', 'dividend-yield', 'asset-allocation', 'risk-tolerance'],

    'psychology': ['mind', 'behavior', 'cognitive', 'therapy', 'anxiety', 'depression', 'stress',
                  'neuron', 'serotonin', 'dopamine', 'freud', 'jung', 'behaviorism', 'ocd',
                  'ptsd', 'bipolar', 'meditation', 'mindfulness', 'personality', 'iq', 'eq',
                  'trauma', 'addiction', 'placebo', 'psychopath', 'empathy', 'motivation',
                  'memory', 'learning', 'perception', 'consciousness', 'subconscious', 'dream',
                  'phobia', 'attachment', 'cognitive-dissonance', 'neuroplasticity', 'clinical',
                  'counseling', 'psychiatrist', 'diagnosis', 'antidepressant', 'stimulus'],

    'fashion': ['wardrobe', 'couture', 'haute-couture', 'tailor', 'textile', 'silk', 'denim',
                'linen', 'cotton', 'knit', 'embroidery', 'accessory', 'handbag', 'heels', 'sneakers',
                'runway', 'vogue', 'trend', 'minimalism', 'bohemian', 'grunge', 'avant-garde',
                'bespoke', 'fast-fashion', 'sustainable-fashion', 'upcycle', 'mannequin', 'boutique',
                'lingerie', 'swimwear', 'formalwear', 'casual', 'androgynous', 'palette', 'texture',
                'pattern', 'drape', 'fit', 'silhouette', 'corset', 'tuxedo', 'kimono', 'sari'],

    'automotive': ['engine', 'transmission', 'horsepower', 'torque', 'sedan', 'suv', 'pickup',
                  'hybrid', 'electric', 'ev', 'charging-station', 'autonomous', 'self-driving',
                  'odometer', 'mph', 'rpm', 'dashboard', 'headlight', 'tailpipe', 'catalytic',
                  'suspension', 'brake', 'tire', 'alloy-wheel', 'aerodynamics', 'fuel-efficiency',
                  'vin', 'dealership', 'lease', 'maintenance', 'oil-change', 'carburetor', 'turbo',
                  'drivetrain', '4wd', 'awd', 'manual-transmission', 'automatic', 'paddle-shifter',
                  'lane-assist', 'adaptive-cruise', 'infotainment', 'carplay', 'android-auto'],

    'real-estate': ['property', 'listing', 'realtor', 'mortgage', 'down-payment', 'appraisal',
                   'zoning', 'condo', 'townhouse', 'single-family', 'multi-family', 'landlord',
                   'tenant', 'lease', 'rent', 'eviction', 'amenities', 'sqft', 'open-house',
                   'closing-costs', 'escrow', 'title', 'home-inspection', 'foreclosure', 'flipping',
                   'remodel', 'renovation', 'blueprint', 'stucco', 'hardwood', 'countertop',
                   'backsplash', 'walk-in-closet', 'master-bedroom', 'curb-appeal', 'hoa', 'mls',
                   'commercial', 'residential', 'industrial', 'mixed-use', 'vacation-home', 'airbnb'],

    'agriculture': ['crop', 'harvest', 'irrigation', 'tractor', 'fertilizer', 'pesticide', 'organic',
                   'gmo', 'livestock', 'pasture', 'greenhouse', 'hydroponics', 'aquaponics', 'compost',
                   'soil', 'arable', 'drought-resistant', 'crop-rotation', 'subsidy', 'agribusiness',
                   'ranch', 'orchard', 'vineyard', 'beekeeping', 'poultry', 'dairy', 'free-range',
                   'permaculture', 'sustainable', 'food-security', 'monoculture', 'polyculture',
                   'harvester', 'plow', 'seedling', 'grafting', 'hybrid', 'heirloom', 'fallow'],

    'space': ['astronomy', 'telescope', 'planet', 'galaxy', 'nebula', 'black-hole', 'light-year',
              'parsec', 'cosmos', 'big-bang', 'dark-matter', 'gravity', 'orbit', 'satellite',
              'spacecraft', 'rover', 'iss', 'nasa', 'spacex', 'elon-musk', 'mars', 'jupiter',
              'saturn', 'milky-way', 'supernova', 'pulsar', 'quasar', 'exoplanet', 'asteroid',
              'comet', 'meteor', 'cosmonaut', 'spacesuit', 'zero-gravity', 'launchpad', 'payload',
              'ion-drive', 'hubble', 'jwst', 'voyager', 'apollo', 'artemis', 'space-tourism'],

    'gaming': ['console', 'pc-gaming', 'vr-gaming', 'esports', 'fps', 'rpg', 'mmorpg', 'pvp', 'pve',
               'sandbox', 'open-world', 'quest', 'npc', 'avatar', 'texture-pack', 'mod', 'dlc',
               'lag', 'ping', 'server', 'respawn', 'hitbox', 'nerf', 'buff', 'grinding', 'loot',
               'raid', 'guild', 'streamer', 'twitch', 'speedrun', 'emulator', 'retro-gaming',
               'indie-game', 'triple-a', 'game-engine', 'unreal-engine', 'unity', 'pixel', 'render',
               'ray-tracing', 'cross-platform', 'controller', 'mechanical-keyboard', 'gaming-mouse'],

    'music': ['melody', 'harmony', 'rhythm', 'tempo', 'pitch', 'chord', 'scale', 'octave', 'genre',
              'classical', 'jazz', 'rock', 'pop', 'hip-hop', 'electronic', 'symphony', 'concerto',
              'opera', 'acoustic', 'amplifier', 'equalizer', 'synthesizer', 'sampler', 'bpm',
              'notation', 'conductor', 'orchestra', 'quartet', 'solo', 'album', 'ep', 'single',
              'vinyl', 'streaming', 'spotify', 'playlist', 'lyrics', 'hook', 'bridge', 'verse',
              'chorus', 'remix', 'cover', 'tuner', 'metronome', 'soundcheck', 'feedback'],

    'history': ['ancient', 'medieval', 'renaissance', 'industrial-revolution', 'colonialism', 'ww1',
                'ww2', 'cold-war', 'civilization', 'empire', 'monarchy', 'revolution', 'treaty',
                'artifact', 'excavation', 'dynasty', 'feudalism', 'crusades', 'slavery', 'abolition',
                'suffrage', 'enlightenment', 'manifest-destiny', 'holocaust', 'armistice', 'archives',
                'primary-source', 'secondary-source', 'historiography', 'anthropology', 'paleontology',
                'fossil', 'hieroglyph', 'cuneiform', 'archeological-dig', 'carbon-dating', 'oral-history',
                'battle', 'conquest', 'colonization', 'independence', 'reformation', 'inquisition'],

    'family': ['mother', 'father', 'parents', 'sister', 'brother', 'son', 'daughter', 'baby', 'grandmother', 'grandfather', 'family', 'friend'],
    
    'body': ['head', 'eyes', 'nose', 'mouth', 'ears', 'arms', 'hands', 'fingers', 'legs', 'feet', 'back', 'stomach'],
    
    'clothes': ['shirt', 'pants', 'shoes', 'socks', 'jacket', 'hat', 'dress', 'skirt', 'coat', 'gloves', 'scarf'],
    
    'food': ['apple', 'banana', 'bread', 'rice', 'milk', 'water', 'coffee', 'tea', 'egg', 'meat', 'fish', 'vegetables'],
    
    'home': ['house', 'room', 'bed', 'table', 'chair', 'sofa', 'door', 'window', 'kitchen', 'bathroom', 'refrigerator', 'lamp'],
    
    'animals': ['dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'chicken', 'elephant', 'lion', 'rabbit'],
    
    'colors': ['red', 'blue', 'yellow', 'green', 'black', 'white', 'orange', 'pink', 'brown', 'gray'],
    
    'numbers': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'twenty', 'thirty', 'fifty', 'hundred'],
    
    'time': ['morning', 'afternoon', 'evening', 'night', 'today', 'tomorrow', 'yesterday', 'hour', 'minute', 'second'],
    
    'weather': ['sun', 'rain', 'cloud', 'wind', 'snow', 'hot', 'cold', 'warm', 'weather', 'sky'],
    
    'jobs': ['teacher', 'doctor', 'nurse', 'student', 'driver', 'cook', 'police', 'farmer', 'worker', 'manager'],
    
    'city': ['city', 'street', 'park', 'school', 'hospital', 'restaurant', 'shop', 'station', 'bank', 'cinema'],
    
    'transport': ['car', 'bus', 'bicycle', 'train', 'plane', 'boat', 'walk', 'drive', 'stop', 'go'],
    
    'actions': ['eat', 'drink', 'sleep', 'go', 'come', 'read', 'write', 'speak', 'listen', 'see', 'buy', 'work', 'play', 'learn'],
    
    'adjectives': ['big', 'small', 'happy', 'sad', 'good', 'bad', 'new', 'old', 'fast', 'slow', 'easy', 'difficult'],
    
    'school': ['book', 'pen', 'pencil', 'paper', 'notebook', 'bag', 'desk', 'teacher', 'student', 'classroom'],
    
    'pronouns': ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'our', 'their'],

    'daily_routines': ['wake up', 'eat breakfast', 'go to school', 'work', 'go home', 'sleep', 
                      'take a shower', 'brush teeth', 'watch TV', 'read a book'],
    
    # Household Items
    'household_items': ['spoon', 'fork', 'knife', 'plate', 'cup', 'bowl', 'towel', 'soap', 
                       'toothbrush', 'pillow', 'blanket', 'clock'],
    
    # Emotions
    'emotions': ['happy', 'sad', 'angry', 'tired', 'hungry', 'thirsty', 'scared', 'excited'],
    
    # Shopping
    'shopping': ['money', 'buy', 'sell', 'shop', 'market', 'price', 'cheap', 'expensive', 
                 'size', 'try on'],
    
    # Hobbies
    'hobbies': ['draw', 'sing', 'dance', 'swim', 'run', 'play football', 'play games', 
                'take photos', 'cook', 'garden'],
    
    # Health
    'health': ['doctor', 'hospital', 'medicine', 'headache', 'stomachache', 'cold', 
               'fever', 'cough', 'pain', 'feel better'],
    
    # Nature
    'nature': ['tree', 'flower', 'grass', 'sun', 'moon', 'star', 'river', 'mountain', 
               'sea', 'cloud'],
    
    # Technology
    'technology': ['phone', 'computer', 'television', 'camera', 'internet', 'email', 
                   'message', 'video', 'photo', 'app'],
    
    # Directions
    'directions': ['left', 'right', 'straight', 'up', 'down', 'near', 'far', 'map', 
                   'street', 'address'],
    
    # Holidays
    'holidays': ['birthday', 'Christmas', 'New Year', 'holiday', 'party', 'present', 
                 'cake', 'decorations', 'music', 'dance'],

    # Classroom Objects
    'classroom': ['blackboard', 'chalk', 'eraser', 'notebook', 'pencil case', 'ruler', 
                 'scissors', 'glue', 'marker', 'stapler'],
    
    # Baby Animals
    'baby_animals': ['puppy', 'kitten', 'cub', 'duckling', 'chick', 'lamb', 'calf', 
                    'foal', 'bunny', 'piglet'],
    
    # Fruits
    'fruits': ['orange', 'grape', 'strawberry', 'pear', 'peach', 'melon', 'pineapple', 
              'cherry', 'lemon', 'watermelon'],
    
    # Vegetables
    'vegetables': ['carrot', 'potato', 'tomato', 'onion', 'cucumber', 'lettuce', 
                  'pepper', 'mushroom', 'corn', 'beans'],
    
    # Shapes
    'shapes': ['circle', 'square', 'triangle', 'rectangle', 'star', 'heart', 'oval', 
              'diamond', 'line', 'arrow'],
    
    # Musical Instruments
    'instruments': ['piano', 'guitar', 'drums', 'violin', 'flute', 'trumpet', 'bell', 
                   'xylophone', 'harmonica', 'tambourine'],
    
    # Sports
    'sports': ['football', 'basketball', 'tennis', 'swimming', 'cycling', 'running', 
              'jumping', 'golf', 'boxing', 'yoga'],
    
    # Rooms in a House
    'rooms': ['bedroom', 'living room', 'dining room', 'bathroom', 'garage', 'garden', 
             'balcony', 'stairs', 'hall', 'office'],
    
    # Office Supplies
    'office': ['pen', 'paper', 'folder', 'envelope', 'calculator', 'calendar', 'printer', 
              'scissors', 'tape', 'clipboard'],
    
    # Seasons
    'seasons': ['spring', 'summer', 'autumn', 'winter', 'rainy', 'sunny', 'snowy', 
               'windy', 'cloudy', 'stormy'],
    
    # Party
    'party': ['balloon', 'candle', 'gift', 'invitation', 'music', 'dance', 'cake', 
             'juice', 'decorations', 'hat'],
    
    # Beach
    'beach': ['sand', 'sea', 'wave', 'shell', 'sun', 'umbrella', 'swim', 'boat', 
             'fish', 'ice cream'],
    
    # Farm
    'farm': ['barn', 'tractor', 'field', 'crops', 'farmer', 'chicken', 'duck', 'goat', 
            'sheep', 'fence'],
    
    # Tools
    'tools': ['hammer', 'nail', 'screwdriver', 'wrench', 'pliers', 'tape measure', 
             'ladder', 'saw', 'brush', 'bucket'],
    
    # Containers
    'containers': ['box', 'bag', 'bottle', 'can', 'jar', 'cup', 'glass', 'plate', 
                  'bowl', 'basket'],

    'function_words': [
        # Pronouns
        'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
        # Articles
        'the', 'a', 'an',
        # Basic verbs
        'am', 'is', 'are', 'was', 'were', 'be', 'have', 'has', 'do', 'does',
        # Prepositions
        'in', 'on', 'at', 'to', 'for', 'of', 'with', 'from', 'by', 'about',
        # Conjunctions
        'and', 'but', 'or', 'so', 'because', 'if',
        # Demonstratives
        'this', 'that', 'these', 'those',
        # Question words
        'who', 'what', 'where', 'when', 'why', 'how',
        # Possessives
        'my', 'your', 'his', 'her', 'its', 'our', 'their',
        # Negation
        'not', 'no', 'yes',
        # Other basics
        'there', 'here', 'all', 'some', 'many', 'one', 'first', 'very', 'too'
    ]
}

import re
from collections import Counter
import pandas as pd
import numpy as np
import spacy
import textstat

nlp = spacy.load("en_core_web_sm")

# Load CEFR word data
cefr_df = pd.read_csv("c:/Users/archi/Desktop/Fiverr/Sanledes/cefr_data.csv")  # Make sure this file exists


def get_word_level(word, cefr_df):
    word_data = cefr_df[cefr_df['word'] == word]
    if not word_data.empty:
        # Return all data for the word as a dictionary
        return word_data.iloc[0].to_dict()
    return None


def categorize_word(word, topic_dict):
    for topic, words in topic_dict.items():
        if topic != 'general' and word in words:
            return topic
    return 'general'



def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# Scale Flesch Reading Ease (0-100) to a 0-10 range
def scale_readability_score(flesch_score):
    return max(0, min(10, (flesch_score / 10)))  # Scaling 0-100 range to 0-10

def get_readability_score(text):
    sentences = text.split('.')  # Basic sentence split
    word_count = len(text.split())
    syllable_count = sum(get_syllables(word) for word in text.split())
    sentence_count = len(sentences)

    # Handle case where there are no sentences
    if sentence_count == 0:
        sentence_count = 1

    # Flesch Reading Ease Formula
    flesch_reading_ease = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)

    # Scale the Flesch Reading Ease score to a 0-10 range
    scaled_readability = scale_readability_score(flesch_reading_ease)

    return scaled_readability

def get_pos_tags(text):
    doc = nlp(text)
    return {token.text: token.pos_ for token in doc if token.is_alpha}

def extract_phrases(text, min_words=3, max_words=5):
    words = text.split()
    phrases = []
    
    for n in range(min_words, max_words + 1):
        phrases.extend([' '.join(words[i:i+n]) for i in range(len(words)-n+1)])
    
    return phrases

def is_valid_phrase(phrase):
    words = phrase.split()
    long_enough = sum(len(word) >= 4 for word in words)
    return long_enough >= len(words) - 1  # Allow one short word

def get_syllables(word):
    try:
        return textstat.syllable_count(word)
    except:
        return 999

def analyze_text(text, cefr_df, topic_dict):
    words = text.split()
    total_words = len(words)
    word_counts = Counter(words)
    pos_dict = get_pos_tags(text)
    
    phrases = extract_phrases(text)
    phrase_counts = Counter(phrases)
    
    results = []
    
    # Analyze individual words
    for word, count in word_counts.items():
        word_data = get_word_level(word, cefr_df)
        raw_freq = count / total_words
        topic = categorize_word(word, topic_dict)
        syllables = get_syllables(word)
        word_len = len(word)
        pos = pos_dict.get(word, 'UNKNOWN')
        readability_score = get_readability_score(word)

        # Create base result dictionary
        result = {
            'word/phrase': word,
            'type': 'word',
            'raw_frequency': raw_freq,
            'count': count,
            'topic': topic,
            'POS': pos,
            'syllables': syllables,
            'readability_score': round(readability_score, 2)
        }
        
        # Add CEFR data if available
        if word_data:
            for col in ['level', 'pos_x', 'headword', 'pos_y', 'CEFR', 
                         'CoreInventory 1', 'CoreInventory 2', 'Threshold', 
                         'Shorthand Code', 'Grammatical Item', 'Sentence Type',
                         'CEFR-J Level', 'Core Inventory', 'EGP', 'GSELO']:
                if col in word_data:
                    result[col] = word_data[col]
        else:
            result['level'] = 'UNKNOWN'
        
        results.append(result)
    
    # Analyze phrases (rest of your existing phrase analysis code)
    common_phrases = [
        phrase for phrase, count in phrase_counts.items()
        if count >= 3 and is_valid_phrase(phrase)
    ]

    for phrase in common_phrases:
        count = phrase_counts[phrase]
        raw_freq = count / total_words

        words_in_phrase = phrase.split()
        syllables = sum(get_syllables(w) for w in words_in_phrase)
        word_count = len(words_in_phrase)

        readability_score = get_readability_score(phrase) 

        # Get levels of component words
        component_levels = []
        for word in words_in_phrase:
            word_data = get_word_level(word, cefr_df)
            if word_data and 'level' in word_data:
                component_levels.append(word_data['level'])

        phrase_level = max(component_levels) if component_levels else 'UNKNOWN'

        results.append({
            'word/phrase': phrase,
            'type': 'phrase',
            'raw_frequency': raw_freq,
            'count': count,
            'level': phrase_level,
            'topic': 'PHRASE',
            'POS': 'NA',
            'syllables': syllables,
            'readability_score': round(readability_score, 2) if readability_score != 'N/A' else 'N/A'
        })
    
    return pd.DataFrame(results)


def add_frequency_score(df):
    print(df.columns)
    df['log_freq'] = np.log10(df['raw_frequency'] + 1e-10)
    min_log = df['log_freq'].min()
    max_log = df['log_freq'].max()
    df['frequency_score'] = 1 + 9 * (df['log_freq'] - min_log) / (max_log - min_log)
    df['frequency_score'] = df['frequency_score'].round().astype(int)
    df['frequency_score'] = df['frequency_score'].clip(1, 10)
    print(df.columns)
    return df

# Main execution
file_path = "c:/Users/archi/Desktop/Fiverr/Sanledes/data.txt"
text = load_text(file_path)

cleaned_text = clean_text(text)

analysis_df = analyze_text(cleaned_text, cefr_df, topic_dict)
scored_df = add_frequency_score(analysis_df)
print(analysis_df.columns)
print(scored_df.columns)


# Lowercase POS
scored_df['POS'] = scored_df['POS'].str.lower()

# Function to handle pos_x and pos_y combining with NaN check
def combine_pos(row):
    pos = row['POS']
    tags = []

    for val in [row['pos_x'], row['pos_y']]:
        if pd.notna(val):
            val_lower = val.lower()
            if val_lower != pos and val_lower not in [tag.lower() for tag in tags]:
                tags.append(val)

    if tags:
        return f"{pos} {','.join(tags)}"
    else:
        return pos

# Apply the logic
scored_df['POS'] = scored_df.apply(combine_pos, axis=1)

# Drop pos_x and pos_y
scored_df = scored_df.drop(columns=['pos_x', 'pos_y'])

def combine_columns(row):
    # Create a set to store unique values (case-insensitive)
    combined_values = set()
    
    # Combine Topic and the three inventory/threshold columns
    for col in ['topic', 'CoreInventory 1', 'CoreInventory 2', 'Threshold']:
        if pd.notna(row[col]):
            # Add the lowercased value to the set
            combined_values.add(row[col].lower())
    
    # Join the unique values with a comma and return
    return ','.join(sorted(combined_values))

# Apply function to combine columns and create the new column
scored_df['topic'] = scored_df.apply(combine_columns, axis=1)

# Drop the original columns if you no longer need them
scored_df = scored_df.drop(columns=['CoreInventory 1', 'CoreInventory 2', 'Threshold'])


scored_df.to_csv("text_analysis_with_phrases.csv", index=False)

print("Top 20 words/phrases with frequency scores:\n")
top_words = scored_df.sort_values('frequency_score', ascending=False).head(20)
for _, row in top_words.iterrows():
    print(f"{row['word/phrase']} ({row['type']}):")
    print(f"  Count: {row['count']}")
    print(f"  Frequency Score: {row['frequency_score']}/10")
    print(f"  CEFR Level: {row['level']}")
    print(f"  Topic: {row['topic']}\n")

print("\nWord count by topic (excluding phrases):")
print(scored_df[scored_df['type'] == 'word']['topic'].value_counts())

print("\nMost common phrases:")
phrases_df = scored_df[scored_df['type'] == 'phrase'].sort_values('count', ascending=False)
print(phrases_df[['word/phrase', 'count', 'level']].head(10))