import sqlite3

DB_NAME = "aicompass.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Definitions Table
    cursor.execute('DROP TABLE IF EXISTS definitions')
    cursor.execute('''
        CREATE TABLE definitions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            definition TEXT,
            example TEXT
        )
    ''')

    # 2. Fun Facts Table
    cursor.execute('DROP TABLE IF EXISTS funfacts')
    cursor.execute('''
        CREATE TABLE funfacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            fun_fact TEXT
        )
    ''')

    # 3. Quiz Questions Table
    cursor.execute('DROP TABLE IF EXISTS quiz_questions')
    cursor.execute('''
        CREATE TABLE quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            question TEXT,
            option_1 TEXT,
            option_2 TEXT,
            option_3 TEXT,
            option_4 TEXT,
            answer TEXT,
            explanation TEXT
        )
    ''')


    definitions_data = [
        # Artificial Intelligence
        (
            'Artificial Intelligence',
            'Artificial Intelligence is the field of computer science focused on building systems that can perform tasks which normally require human intelligence, such as reasoning, learning, and problem solving.',
            'Virtual assistants like Siri or Alexa answering questions and understanding spoken commands.'
        ),
        (
            'Supervised Learning',
            'Supervised learning is a type of machine learning where the model is trained on labelled data, meaning each input comes paired with the correct answer so the model can learn from mistakes.',
            'Training a spam filter by showing it thousands of emails already marked as spam or not spam.'
        ),
        (
            'Unsupervised Learning',
            'Unsupervised learning is when a model explores data on its own without any pre-labelled answers, discovering hidden patterns or groupings by itself.',
            'Grouping customers into segments based on shopping behaviour without any predefined categories.'
        ),
        (
            'Overfitting',
            'Overfitting happens when a model learns the training data so thoroughly that it picks up noise and quirks, causing it to perform poorly when given new, unseen data.',
            'A model that scores perfectly on training examples but fails badly when tested on fresh data.'
        ),
        (
            'AI Agent',
            'An AI agent is a system that can perceive its environment, make decisions, and take actions on its own to reach a defined goal, often completing multi-step tasks without constant human input.',
            'An AI assistant that browses the web, fills in forms, and books flights on behalf of a user.'
        ),

        # Machine Learning
        (
            'Machine Learning',
            'Machine learning is a branch of artificial intelligence in which systems learn patterns directly from data and improve over time without being explicitly programmed for every situation.',
            'An email spam filter that gets better at identifying junk mail the more data it processes.'
        ),
        (
            'Feature',
            'In machine learning, a feature is an individual measurable property of the data that the model uses as input to make predictions or decisions.',
            'Using square footage, number of bedrooms, and location as features to predict house prices.'
        ),
        (
            'Label',
            'A label is the correct output or answer that corresponds to a training example, telling the model what it should have predicted for that input.',
            'Marking emails as spam or not spam so a classifier knows the right answer during training.'
        ),
        (
            'Gradient Descent',
            'Gradient descent is the optimisation algorithm used during training where a model repeatedly adjusts its internal values in small steps to reduce prediction errors over time.',
            'A neural network slowly adjusting weights after each batch of training examples to get closer to accurate predictions.'
        ),
        (
            'Regularisation',
            'Regularisation is a technique applied during training to discourage a model from becoming overly complex, reducing the risk of overfitting and helping it generalise to new data.',
            'Adding an L2 penalty to a regression model so it does not assign too much importance to any single feature.'
        ),

        # Deep Learning
        (
            'Deep Learning',
            'Deep learning is a subfield of machine learning that uses neural networks with many stacked layers to automatically learn complex patterns, especially in data like images, audio, and text.',
            'A deep learning model recognising faces in photos by learning edges, shapes, and features across many layers.'
        ),
        (
            'Neural Network',
            'A neural network is a computational model loosely inspired by the human brain, made up of interconnected nodes organised in layers that process and transform information.',
            'A network trained to classify handwritten digits by passing pixel values through multiple layers of nodes.'
        ),
        (
            'Convolutional Neural Network',
            'A Convolutional Neural Network is a type of deep learning model designed for processing grid-like data such as images, using filters to detect patterns like edges, textures, and shapes.',
            'A CNN powering a mobile app that can identify plant species from a photo taken by the user.'
        ),
        (
            'Recurrent Neural Network',
            'A Recurrent Neural Network is a type of neural network built to handle sequential data by maintaining a memory of previous inputs, making it useful for tasks like language and time series.',
            'An RNN generating text one word at a time by considering all the words it has already produced.'
        ),
        (
            'Dropout',
            'Dropout is a regularisation method used during neural network training where random neurons are temporarily deactivated in each pass, forcing the network to learn more robust and distributed features.',
            'Applying a 50 percent dropout rate during training so the model does not rely too heavily on any single neuron.'
        ),

        # Natural Language Processing
        (
            'Natural Language Processing',
            'Natural Language Processing is the area of artificial intelligence that helps computers read, understand, interpret, and generate human language in a way that is both meaningful and useful.',
            'A chatbot that reads customer messages, understands the intent, and responds with relevant answers automatically.'
        ),
        (
            'Tokenisation',
            'Tokenisation is the process of splitting text into smaller units called tokens, such as words or subwords, which a language model can then process numerically.',
            "Breaking the sentence 'I love AI' into the tokens ['I', 'love', 'AI'] before feeding it to a model."
        ),
        (
            'Sentiment Analysis',
            'Sentiment analysis is an NLP task that identifies and extracts the emotional tone of a piece of text, determining whether it is positive, negative, or neutral.',
            'Automatically scanning product reviews to gauge whether customers are generally happy or unhappy.'
        ),
        (
            'Named Entity Recognition',
            'Named Entity Recognition is the NLP task of identifying and classifying specific terms in text into categories such as people, organisations, locations, and dates.',
            "Scanning a news article and automatically tagging names like 'Google', 'London', and 'Sundar Pichai' with their entity types."
        ),
        (
            'Machine Translation',
            'Machine translation is the use of AI to automatically convert text or speech from one human language to another while preserving its meaning as closely as possible.',
            'Google Translate converting a paragraph of French text into English in real time.'
        ),

        # Computer Vision
        (
            'Computer Vision',
            'Computer vision is the field of artificial intelligence that trains machines to interpret and understand visual information from images and videos, much like the human visual system does.',
            'A self-driving car using cameras and computer vision models to detect pedestrians, traffic signs, and other vehicles.'
        ),
        (
            'Object Detection',
            'Object detection is a computer vision task where a model identifies and locates multiple objects within an image or video frame, typically drawing a bounding box around each one.',
            'A security camera system that automatically highlights people and vehicles appearing in footage.'
        ),
        (
            'Image Segmentation',
            'Image segmentation is the process of dividing an image into meaningful regions by assigning each pixel to a category, giving the model a detailed understanding of what is where in the scene.',
            'A medical imaging tool that colours each organ a different shade so doctors can clearly see boundaries.'
        ),
        (
            'Optical Character Recognition',
            'Optical Character Recognition is the technology that converts images of printed or handwritten text into machine-readable digital text that can be searched or edited.',
            'A mobile app photographing a printed receipt and automatically extracting the total amount and date.'
        ),
        (
            'Facial Recognition',
            'Facial recognition is a biometric technology that identifies or verifies a person by analysing and comparing patterns in their facial features against a stored database.',
            'A smartphone unlocking itself by comparing the owner\'s face captured by the front camera to a saved reference.'
        ),

        # Reinforcement Learning
        (
            'Reinforcement Learning',
            'Reinforcement learning is a type of machine learning where an agent learns by interacting with an environment, receiving rewards for good actions and penalties for poor ones, gradually improving its strategy.',
            'Training a robot to walk by rewarding it whenever it successfully moves forward without falling over.'
        ),
        (
            'Reward Function',
            'The reward function is the signal in reinforcement learning that tells the agent how good or bad a particular action was, guiding it toward behaviours that maximise long-term success.',
            'In a chess-playing AI, giving a positive reward for capturing pieces and a large reward for winning the game.'
        ),
        (
            'Policy',
            'In reinforcement learning, a policy is the strategy or set of rules the agent follows to decide which action to take given the current state of the environment.',
            'A game-playing AI following a learned policy that says to always move aggressively when it has more pieces than the opponent.'
        ),
        (
            'Exploration vs Exploitation',
            'Exploration versus exploitation is the trade-off in reinforcement learning between trying new actions to discover better strategies and using what has already been learned to maximise known rewards.',
            'A recommendation system occasionally showing users new content they have never seen rather than always showing their proven favourites.'
        ),
        (
            'Q-Learning',
            'Q-learning is a reinforcement learning algorithm where the agent learns the value of taking specific actions in specific states, building a table of expected future rewards to guide its decisions.',
            'An AI learning to play a video game by assigning a value to every possible move at every moment and always picking the highest-value option.'
        ),

        # Neural Networks
        (
            'Activation Function',
            'An activation function is applied to a neuron\'s output to introduce non-linearity into the network, allowing it to learn complex patterns that a simple linear model could not capture.',
            'Using the ReLU function so that any negative value a neuron produces is replaced with zero, keeping the signal sparse and efficient.'
        ),
        (
            'Backpropagation',
            'Backpropagation is the algorithm used to train neural networks by calculating how much each weight contributed to the prediction error and then adjusting all weights accordingly.',
            'After a network misclassifies an image, backpropagation traces the error backward through every layer and nudges each connection weight slightly in the right direction.'
        ),
        (
            'Loss Function',
            'A loss function measures the difference between the model\'s predicted output and the actual correct answer, giving a single number that represents how wrong the model currently is.',
            'Using mean squared error to measure how far a house price prediction is from the real sale price.'
        ),
        (
            'Epoch',
            'An epoch is one complete pass through the entire training dataset during the learning process; models typically train for many epochs until performance stops improving.',
            'Running 50 epochs means the model has seen every training example 50 times before training is considered finished.'
        ),
        (
            'Batch Size',
            'Batch size refers to the number of training examples the model processes together before updating its weights, balancing the trade-off between training speed and stability.',
            'Using a batch size of 32 so the model updates its weights after every 32 images rather than waiting to see all images first.'
        ),

        # Generative AI
        (
            'Generative AI',
            'Generative AI refers to artificial intelligence systems that can create new content such as text, images, audio, or video by learning the underlying patterns in large amounts of existing data.',
            'DALL-E producing a photorealistic image of an astronaut riding a horse based solely on a text description.'
        ),
        (
            'Generative Adversarial Network',
            'A Generative Adversarial Network is a deep learning framework where two neural networks, a generator and a discriminator, compete with each other, pushing the generator to produce increasingly realistic outputs.',
            'A GAN trained on celebrity faces generating brand new, photorealistic portraits of people who do not actually exist.'
        ),
        (
            'Diffusion Model',
            'A diffusion model is a type of generative AI that learns to reverse a gradual noise-adding process, allowing it to produce high-quality images or audio from pure random noise.',
            'Stable Diffusion starting from a field of random pixels and progressively refining them into a detailed landscape painting.'
        ),
        (
            'Prompt Engineering',
            'Prompt engineering is the practice of carefully designing the text inputs given to a generative AI model in order to guide it toward producing accurate, useful, or creative outputs.',
            "Writing a detailed instruction like 'Explain quantum computing to a 10-year-old using a toy analogy' to get a clearer and more appropriate response."
        ),
        (
            'Hallucination',
            'Hallucination in AI refers to when a generative model produces information that sounds confident and plausible but is factually incorrect or entirely made up.',
            'A language model confidently citing a research paper with a real-sounding title and author that does not actually exist anywhere.'
        ),

        # AI Ethics
        (
            'Bias in AI',
            'Bias in AI occurs when a model produces systematically unfair or skewed results, often because the training data did not represent all groups equally or reflected existing societal inequalities.',
            'A hiring algorithm trained mostly on resumes from men rating female applicants lower even when qualifications are identical.'
        ),
        (
            'Explainability',
            'Explainability in AI refers to the degree to which the reasoning behind a model\'s decision can be understood and communicated clearly to the people affected by it.',
            'A loan rejection system that shows applicants exactly which factors, such as credit score or income ratio, led to the refusal.'
        ),
        (
            'Fairness',
            'Fairness in AI means ensuring that a model\'s outputs do not systematically disadvantage any particular group of people based on attributes like race, gender, or age.',
            'Auditing a recidivism prediction model to confirm it does not predict higher reoffending rates for one racial group over another when actual risk is equal.'
        ),
        (
            'Privacy in AI',
            'Privacy in AI is the principle that AI systems should collect, use, and store personal data in ways that respect individuals\' rights and minimise the risk of misuse or exposure.',
            'Federated learning allowing a model to train across many devices without ever uploading users\' personal data to a central server.'
        ),
        (
            'AI Alignment',
            'AI alignment is the challenge of ensuring that an AI system\'s goals, behaviours, and values match the intentions and best interests of the humans it is designed to serve.',
            'Researchers designing reward functions carefully so a robot assistant helps with household tasks without causing unintended harm in pursuit of a narrowly defined goal.'
        ),

        # Large Language Models
        (
            'Large Language Model',
            'A Large Language Model is an AI system trained on enormous amounts of text data, enabling it to understand and generate human-like language for a wide range of tasks.',
            'ChatGPT answering complex questions, writing code, summarising documents, and holding conversations in multiple languages.'
        ),
        (
            'Transformer Architecture',
            'The Transformer is the neural network architecture that underpins most modern language models, using a mechanism called attention to relate every word in a sequence to every other word at once.',
            'GPT-4 reading an entire paragraph and understanding how the pronoun "it" in the last sentence refers back to a subject mentioned at the beginning.'
        ),
        (
            'Attention Mechanism',
            'The attention mechanism allows a model to weigh the importance of different parts of the input when producing each part of the output, helping it capture long-range relationships in language.',
            'A translation model paying extra attention to the subject of a sentence when choosing the correct verb form in the target language.'
        ),
        (
            'Fine-Tuning',
            'Fine-tuning is the process of taking a pre-trained language model and continuing its training on a smaller, task-specific dataset so it becomes more accurate for a particular use case.',
            'Taking a general-purpose language model and fine-tuning it on medical literature so it gives more precise answers to clinical questions.'
        ),
        (
            'Retrieval-Augmented Generation',
            'Retrieval-Augmented Generation is a technique that combines a language model with a search system, allowing the model to look up relevant facts before generating a response rather than relying purely on memorised knowledge.',
            "An AI customer support bot searching a company's help documentation in real time before composing its reply to a user's question."
        ),
    ]

    # ── FUN FACTS (50 rows, 5 per topic) ──────────────────────────────────────

    funfacts_data = [
        # Artificial Intelligence
        (
            'Artificial Intelligence',
            "The term 'Artificial Intelligence' was first introduced at a workshop at Dartmouth College in 1956, which is why many people consider that the official birthday of the field."
        ),
        (
            'Artificial Intelligence',
            "Back in 1997, an AI called Deep Blue became the first computer to beat a reigning world chess champion in a match, defeating Garry Kasparov in front of a global audience."
        ),
        (
            'Artificial Intelligence',
            "AI research went through two long periods of reduced funding and enthusiasm known as 'AI winters', first in the 1970s and again in the late 1980s, before bouncing back stronger than ever."
        ),
        (
            'Artificial Intelligence',
            "In 2022, an AI-generated artwork called 'Theatre D'Opera Spatial' won first place in a fine arts competition in Colorado, sparking a huge conversation about creativity and authorship."
        ),
        (
            'Artificial Intelligence',
            "Researchers at Google DeepMind built an AI called AlphaFold that predicted the 3D structure of nearly every known protein, a problem scientists had been working on for over 50 years."
        ),

        # Machine Learning
        (
            'Machine Learning',
            "Spam filters were one of the earliest widely used machine learning applications, and they were already classifying millions of emails before most people had even heard the term 'machine learning'."
        ),
        (
            'Machine Learning',
            "Netflix estimates that its machine learning recommendation system saves the company around one billion dollars per year by keeping subscribers engaged and reducing the number who cancel."
        ),
        (
            'Machine Learning',
            "In many real-world projects, data scientists spend up to 80 percent of their time just cleaning and preparing data, with the actual model training taking up only a small fraction of the effort."
        ),
        (
            'Machine Learning',
            "The Kaggle data science competition platform has hosted challenges where gradient boosting models won so consistently that it became something of a running joke in the community."
        ),
        (
            'Machine Learning',
            "Machine learning models have been trained to predict earthquakes, detect crop diseases from drone footage, and even identify illegal fishing vessels from satellite imagery."
        ),

        # Deep Learning
        (
            'Deep Learning',
            "The idea of artificial neural networks actually dates back to 1943, but deep learning only really took off around 2012 when advances in GPU computing made training large networks practical."
        ),
        (
            'Deep Learning',
            "In 2012, a deep learning model called AlexNet slashed the error rate on the ImageNet image classification challenge by such a large margin that it shocked the entire computer vision community."
        ),
        (
            'Deep Learning',
            "GPT-4, one of the most powerful language models ever built, is estimated to have around 1.8 trillion parameters, which are the individual adjustable values the model learns during training."
        ),
        (
            'Deep Learning',
            "Deep learning models trained on games like Go and Chess have not just beaten human world champions but reached levels of play so advanced that professionals now study AI games to improve their own skills."
        ),
        (
            'Deep Learning',
            "Generative Adversarial Networks, invented in 2014, work by pitting two networks against each other, and the competition between them is what drives the generator to produce increasingly convincing outputs."
        ),

        # Natural Language Processing
        (
            'Natural Language Processing',
            "Google Translate now supports over 100 languages and processes more than 100 billion words every single day, relying almost entirely on deep learning and transformer models."
        ),
        (
            'Natural Language Processing',
            "BERT, a language model released by Google in 2018, was so effective that it improved performance on nearly every standard NLP benchmark almost overnight, changing how the field approached language tasks."
        ),
        (
            'Natural Language Processing',
            "Modern NLP models can detect sarcasm in text, a task that many humans struggle with in writing, by picking up on subtle patterns in word choice and sentence structure."
        ),
        (
            'Natural Language Processing',
            "The autocorrect feature on your phone is a form of NLP, and early versions from the 1990s were already using statistical models to predict the word you most likely intended to type."
        ),
        (
            'Natural Language Processing',
            "Language models can now pass the bar exam, write functioning code, and summarise lengthy legal contracts, tasks that were considered exclusively within the domain of highly trained professionals just a decade ago."
        ),

        # Computer Vision
        (
            'Computer Vision',
            "The first image recognition system capable of reading handwritten postal codes was deployed by the US Postal Service in the 1990s, processing millions of envelopes per day automatically."
        ),
        (
            'Computer Vision',
            "Modern facial recognition systems can identify a person in a crowd in under a second, even accounting for changes in lighting, angle, and whether the person is wearing glasses."
        ),
        (
            'Computer Vision',
            "Computer vision models trained on medical images can detect certain types of cancer, diabetic retinopathy, and skin conditions with accuracy that rivals or sometimes exceeds that of specialist doctors."
        ),
        (
            'Computer Vision',
            "Self-driving vehicles typically combine computer vision with radar and lidar sensors, since cameras alone can struggle with heavy rain or low-light conditions where other sensors still work reliably."
        ),
        (
            'Computer Vision',
            "Retailers are experimenting with stores that use computer vision to track exactly which items shoppers pick up, allowing customers to simply walk out and be charged automatically with no checkout needed."
        ),

        # Reinforcement Learning
        (
            'Reinforcement Learning',
            "DeepMind's AlphaGo became the first AI to defeat a professional Go player in 2016, a milestone many experts had predicted would not happen for at least another decade."
        ),
        (
            'Reinforcement Learning',
            "Reinforcement learning agents have been trained to play classic Atari games from scratch using only raw pixel input and a score signal, eventually surpassing human expert performance on dozens of titles."
        ),
        (
            'Reinforcement Learning',
            "OpenAI built a robot hand called Dactyl that learned to solve a Rubik's Cube using reinforcement learning, which is impressive because the physical dexterity required is very challenging to program directly."
        ),
        (
            'Reinforcement Learning',
            "AlphaZero, a reinforcement learning system, taught itself chess from scratch in about four hours with no human knowledge beyond the basic rules, then convincingly defeated the world's best chess programs."
        ),
        (
            'Reinforcement Learning',
            "Reinforcement learning is being used to optimise the cooling systems in Google's data centres, and it has reduced energy consumption for cooling by around 40 percent compared to human-managed systems."
        ),

        # Neural Networks
        (
            'Neural Networks',
            "The human brain contains roughly 86 billion neurons, each connected to thousands of others. Artificial neural networks are loosely inspired by this structure but are far simpler in comparison."
        ),
        (
            'Neural Networks',
            "The concept of backpropagation, the algorithm that makes training deep neural networks practical, was popularised in a landmark 1986 paper and remains the core training method used in modern AI."
        ),
        (
            'Neural Networks',
            "A single modern GPU can perform the matrix multiplications needed to run a neural network billions of times faster than a standard CPU, which is why graphics cards became the workhorse of AI research."
        ),
        (
            'Neural Networks',
            "Neural networks used in music generation have been trained to compose pieces in the style of specific composers, and some compositions have fooled listeners into thinking they were written by a human."
        ),
        (
            'Neural Networks',
            "Some very large neural networks have so many parameters that if you printed each one on a standard sheet of paper and stacked them up, the pile would be taller than Mount Everest."
        ),

        # Generative AI
        (
            'Generative AI',
            "The first widely recognised GAN was invented by Ian Goodfellow in 2014, and the idea reportedly came to him during an argument at a bar that he resolved by going home and coding it up that same night."
        ),
        (
            'Generative AI',
            "AI-generated music has already been used in commercial advertisements, film scores, and video game soundtracks, with some tools able to produce a full background track from a simple text description."
        ),
        (
            'Generative AI',
            "Deepfake technology, which uses generative AI to swap faces in video, was originally developed for legitimate research but quickly became a concern for misinformation and is now heavily studied for detection methods."
        ),
        (
            'Generative AI',
            "Midjourney, DALL-E, and Stable Diffusion can each generate thousands of unique images per minute across their servers, collectively producing more visual art in a day than all human artists combined could manage."
        ),
        (
            'Generative AI',
            "Some generative AI models have been used by pharmaceutical companies to design entirely new candidate drug molecules, dramatically speeding up the early stages of drug discovery research."
        ),

        # AI Ethics
        (
            'AI Ethics',
            "A widely studied 2018 audit called 'Gender Shades' found that commercial facial recognition systems from major tech companies had significantly higher error rates for darker-skinned women than for lighter-skinned men."
        ),
        (
            'AI Ethics',
            "The European Union's AI Act, which began coming into force in 2024, is one of the world's first comprehensive laws to regulate AI systems based on their potential risk to people's rights and safety."
        ),
        (
            'AI Ethics',
            "Researchers have found that simply changing the perceived name on an identical resume from a traditionally white-sounding name to a Black-sounding name can affect how AI hiring tools score the candidate."
        ),
        (
            'AI Ethics',
            "The concept of 'explainable AI' has become increasingly important in healthcare, where doctors and patients want to understand why an AI system recommended a particular diagnosis or treatment path."
        ),
        (
            'AI Ethics',
            "A thought experiment called the 'paperclip maximiser', proposed by philosopher Nick Bostrom, illustrates how an AI given a simple goal could cause catastrophic harm if its values are not carefully aligned with human wellbeing."
        ),

        # Large Language Models
        (
            'Large Language Models',
            "GPT-1, released by OpenAI in 2018, had 117 million parameters. Just five years later, models like GPT-4 are estimated to have over a trillion parameters, representing an extraordinary leap in scale."
        ),
        (
            'Large Language Models',
            "The training data for large language models is so vast that if you tried to read it all at a pace of one book per day, it would take you thousands of years to get through it."
        ),
        (
            'Large Language Models',
            "Large language models can now pass professional examinations including the US Medical Licensing Exam, the bar exam, and the CFA financial analyst exam, often scoring in the top percentiles."
        ),
        (
            'Large Language Models',
            "Claude, Anthropic's AI assistant, was built with a focus on being honest and safe, using a training approach called Constitutional AI that teaches the model to evaluate and improve its own responses."
        ),
        (
            'Large Language Models',
            "Despite their impressive abilities, large language models have no persistent memory between conversations by default, meaning they start completely fresh each time and have no recollection of previous chats."
        ),
    ]

    # ── QUIZ QUESTIONS (50 rows, 5 per topic) ─────────────────────────────────
    # answer field is the correct option number as a string: '1', '2', '3', or '4'

    quiz_data = [
        # Artificial Intelligence
        (
            'Artificial Intelligence',
            "Who is credited with coining the term 'Artificial Intelligence' at the Dartmouth Conference in 1956?",
            'Alan Turing', 'John McCarthy', 'Marvin Minsky', 'Geoffrey Hinton',
            '2',
            "John McCarthy organised the 1956 Dartmouth Conference and introduced the term 'Artificial Intelligence'. Alan Turing laid earlier theoretical groundwork, but McCarthy gave the field its name."
        ),
        (
            'Artificial Intelligence',
            'What does an AI agent do that makes it different from a simple AI model?',
            'It only answers questions',
            'It takes actions and makes decisions to reach a goal',
            'It stores data in a database',
            'It translates text between languages',
            '2',
            'An AI agent goes beyond just producing outputs. It perceives its environment, makes decisions, and takes sequences of actions on its own to accomplish a goal, which is fundamentally different from a model that only responds to a single input.'
        ),
        (
            'Artificial Intelligence',
            'Which of the following is the best real-world example of supervised learning?',
            'Grouping news articles by topic automatically',
            'Predicting house prices using labelled sales data',
            'A robot exploring a maze by trial and error',
            'Reducing a dataset from 100 columns to 10',
            '2',
            'Supervised learning requires labelled training data where the correct output is already known. Predicting house prices from historical sales with known prices is a classic supervised learning task.'
        ),
        (
            'Artificial Intelligence',
            'What is the main reason overfitting is a problem in machine learning?',
            'It makes the model train too slowly',
            'The model performs well on training data but poorly on new data',
            'It causes the model to use too much memory',
            'The model ignores the training data entirely',
            '2',
            'Overfitting happens when a model learns the training data too closely, including its noise and quirks. It appears to perform well during training but fails to generalise when it encounters data it has never seen before.'
        ),
        (
            'Artificial Intelligence',
            "Which of the following best describes what 'AI alignment' means?",
            'Making sure AI hardware meets technical standards',
            "Ensuring an AI system's goals and behaviour match human intentions",
            'Training AI on multiple languages at once',
            'Connecting different AI systems together',
            '2',
            "AI alignment is about making sure that as AI systems become more capable, their goals, decisions, and behaviours remain in line with what humans actually want and value, rather than pursuing objectives that could be harmful."
        ),

        # Machine Learning
        (
            'Machine Learning',
            'What is machine learning?',
            'A type of computer hardware used to speed up calculations',
            'A branch of AI where systems learn patterns from data and improve over time',
            'A programming language designed for data analysis',
            'A database system for storing large amounts of information',
            '2',
            'Machine learning is a branch of artificial intelligence where systems improve at tasks by learning patterns from data, rather than being explicitly programmed with every rule. The more data they process, the better they typically get.'
        ),
        (
            'Machine Learning',
            "What is a 'feature' in a machine learning dataset?",
            'The final prediction made by the model',
            'An individual measurable property used as input to the model',
            'The number of examples in the dataset',
            'The error rate of the model after training',
            '2',
            'A feature is one of the input variables the model uses to make a prediction. For example, when predicting house prices, features might include square footage, number of bedrooms, and neighbourhood.'
        ),
        (
            'Machine Learning',
            'What does gradient descent do during model training?',
            'It shuffles the training data before each epoch',
            "It repeatedly adjusts model weights to reduce prediction error",
            'It removes unnecessary features from the dataset',
            'It divides data into training and test sets',
            '2',
            "Gradient descent is the optimisation algorithm used to train most machine learning models. It calculates how wrong the model is and then nudges the model's weights slightly in the direction that reduces that error, repeating this until performance improves."
        ),
        (
            'Machine Learning',
            'Why is regularisation used when training a machine learning model?',
            "To increase the model's complexity so it learns more details",
            'To prevent overfitting by discouraging the model from becoming too complex',
            'To speed up the training process on large datasets',
            'To convert text data into numerical form the model can process',
            '2',
            'Regularisation adds a penalty for complexity during training, encouraging the model to stay simpler. This helps it avoid memorising the training data and instead learn patterns that generalise well to new, unseen examples.'
        ),
        (
            'Machine Learning',
            'Which of the following tasks is a classification problem?',
            'Predicting the exact temperature tomorrow',
            "Estimating a car's fuel efficiency from engine specs",
            'Deciding whether an email is spam or not spam',
            "Forecasting a company's quarterly revenue",
            '3',
            'Classification is about assigning inputs to discrete categories. Deciding whether an email is spam or not spam produces one of two labels, making it a classic classification task. The other options involve predicting continuous numerical values, which is regression.'
        ),

        # Deep Learning
        (
            'Deep Learning',
            'What is deep learning?',
            'A method for manually programming rules into a computer',
            'A machine learning approach using multi-layered neural networks to learn complex patterns',
            'A database technique for organising large datasets',
            'A tool for visualising data in charts and graphs',
            '2',
            'Deep learning uses neural networks with many layers stacked on top of each other. Each layer learns increasingly abstract features from the data, allowing the model to handle complex tasks like image recognition and language understanding automatically.'
        ),
        (
            'Deep Learning',
            'What type of neural network is most commonly used for image recognition tasks?',
            'Recurrent Neural Network',
            'Convolutional Neural Network',
            'Generative Adversarial Network',
            'Transformer',
            '2',
            'Convolutional Neural Networks are specifically designed for processing grid-like data such as images. They use filters to detect patterns like edges, shapes, and textures across an image, making them highly effective for visual tasks.'
        ),
        (
            'Deep Learning',
            'What is the purpose of the dropout technique in neural networks?',
            'To remove unnecessary columns from the training dataset',
            'To prevent overfitting by randomly deactivating neurons during training',
            'To speed up inference after the model is trained',
            'To convert continuous values into categorical labels',
            '2',
            'Dropout randomly switches off a proportion of neurons during each training pass. This forces the network to learn redundant representations and prevents it from relying too heavily on any single neuron, which helps reduce overfitting.'
        ),
        (
            'Deep Learning',
            'What kind of data is a Recurrent Neural Network best suited for?',
            'Grid-like data such as images',
            'Sequential data such as text or time series',
            'Tabular data with fixed columns',
            'Graph-structured data with nodes and edges',
            '2',
            'Recurrent Neural Networks have a form of memory that allows them to consider previous inputs when processing the current one. This makes them well suited for sequences like text, audio, or time-series data where order matters.'
        ),
        (
            'Deep Learning',
            'In a neural network, what does an activation function do?',
            'It determines how many layers the network will have',
            'It introduces non-linearity so the network can learn complex patterns',
            'It calculates the final loss after each training epoch',
            'It shuffles the training data before the next pass',
            '2',
            'Without activation functions, a neural network with many layers would behave the same as a single-layer linear model. Activation functions introduce non-linearity, allowing the network to learn and represent far more complex relationships in the data.'
        ),

        # Natural Language Processing
        (
            'Natural Language Processing',
            'What is Natural Language Processing?',
            'A method for compressing large image files',
            'The AI field focused on helping computers understand and generate human language',
            'A technique for speeding up database queries',
            'A programming framework for building mobile apps',
            '2',
            'Natural Language Processing is the branch of AI that deals with the interaction between computers and human language. It covers tasks like understanding text, translating languages, answering questions, and generating coherent writing.'
        ),
        (
            'Natural Language Processing',
            'What does tokenisation do in an NLP pipeline?',
            'It converts images into descriptive text',
            'It splits text into smaller units like words or subwords for the model to process',
            'It scores the sentiment of a sentence as positive or negative',
            'It identifies the language a piece of text is written in',
            '2',
            'Tokenisation is the first step in most NLP pipelines. It breaks raw text into tokens, which might be individual words, punctuation marks, or subword pieces, so the model can convert them into numbers and begin processing them.'
        ),
        (
            'Natural Language Processing',
            'What is the goal of sentiment analysis?',
            'To translate text from one language to another',
            'To identify the emotional tone of a piece of text',
            'To extract names of people and places from a document',
            'To summarise a long document into a few sentences',
            '2',
            'Sentiment analysis determines whether the overall feeling expressed in a piece of text is positive, negative, or neutral. It is widely used for analysing customer reviews, social media posts, and survey responses at scale.'
        ),
        (
            'Natural Language Processing',
            'What does Named Entity Recognition identify in a text?',
            'The overall topic or subject matter of the document',
            'Specific entities like people, organisations, and locations',
            'The grammatical structure of each sentence',
            'Whether the text is formal or informal in tone',
            '2',
            'Named Entity Recognition scans text and identifies and classifies specific terms into categories such as person names, company names, geographic locations, dates, and quantities. It is essential for information extraction tasks.'
        ),
        (
            'Natural Language Processing',
            'Which major architectural breakthrough significantly improved machine translation and most other NLP tasks from 2017 onward?',
            'Recurrent Neural Networks',
            'Decision Trees',
            'The Transformer',
            'K-Means Clustering',
            '3',
            "The Transformer architecture, introduced in the paper 'Attention Is All You Need' in 2017, replaced RNNs as the dominant approach for NLP. Its attention mechanism allows the model to consider the entire input sequence at once, dramatically improving quality."
        ),

        # Computer Vision
        (
            'Computer Vision',
            'What is computer vision?',
            'A branch of AI that helps computers interpret and understand visual information from images and videos',
            'A method for converting speech into text',
            'A technique for speeding up graphics rendering in video games',
            'A system for organising and tagging large photo libraries',
            '1',
            'Computer vision is the field of AI that trains machines to see and interpret the visual world. It covers tasks like recognising objects, detecting faces, reading text in images, and understanding video content.'
        ),
        (
            'Computer Vision',
            'What is the difference between image classification and object detection?',
            'Image classification labels the whole image while object detection locates and labels multiple objects within it',
            'Image classification is faster while object detection is more accurate',
            'Object detection only works on videos while classification works on still images',
            'There is no meaningful difference between the two tasks',
            '1',
            'Image classification assigns a single label to an entire image. Object detection goes further by identifying multiple objects within the same image and drawing a bounding box around each one, indicating exactly where each object is located.'
        ),
        (
            'Computer Vision',
            'What does Optical Character Recognition allow a computer to do?',
            'Generate realistic images from text descriptions',
            'Convert images of printed or handwritten text into editable digital text',
            'Identify emotions on a person\'s face in a photo',
            'Detect and track moving objects in a video stream',
            '2',
            'Optical Character Recognition reads the visual appearance of characters in an image and converts them into machine-readable text. It is used in everything from scanning documents to reading number plates and translating text captured by a camera.'
        ),
        (
            'Computer Vision',
            'Which sensor is commonly used alongside cameras in self-driving vehicles to improve safety in poor visibility conditions?',
            'Infrared thermometer',
            'Lidar',
            'Barometer',
            'Gyroscope',
            '2',
            'Lidar sends out laser pulses and measures how long they take to bounce back, building a detailed 3D map of the surroundings. Unlike cameras, lidar works well in low-light or foggy conditions, which is why autonomous vehicles typically combine both technologies.'
        ),
        (
            'Computer Vision',
            'What is image segmentation?',
            'Splitting a dataset of images into training and test sets',
            'Assigning a category label to every individual pixel in an image',
            'Reducing the resolution of an image to save storage space',
            'Detecting whether two images show the same person',
            '2',
            'Image segmentation goes beyond detecting where objects are and instead labels every single pixel in the image with a category. This gives the model a precise, detailed understanding of the scene, which is especially useful in medical imaging and autonomous driving.'
        ),

        # Reinforcement Learning
        (
            'Reinforcement Learning',
            'What is reinforcement learning?',
            'A method where the model learns by memorising a fixed set of rules',
            'A type of learning where an agent improves by receiving rewards and penalties from its environment',
            'A technique for labelling large datasets quickly',
            'A way of training models using only unlabelled data',
            '2',
            'In reinforcement learning, an agent takes actions in an environment and receives feedback in the form of rewards for good outcomes and penalties for poor ones. Over time it learns a strategy that maximises cumulative reward.'
        ),
        (
            'Reinforcement Learning',
            "What is a 'reward function' in reinforcement learning?",
            'A measure of how many parameters the model has',
            "The signal that tells the agent how good or bad its most recent action was",
            'The set of all possible states the environment can be in',
            'A function that converts raw observations into features',
            '2',
            "The reward function is what guides the agent's learning. It assigns a numerical score to each action in a given state, and the agent's goal is to learn a policy that maximises the total reward it receives over time."
        ),
        (
            'Reinforcement Learning',
            "What does the term 'policy' mean in the context of reinforcement learning?",
            'The rules that determine how training data is collected',
            'The strategy the agent follows to decide which action to take in each state',
            'The penalty applied when the agent makes a mistake',
            'The maximum number of steps allowed in each training episode',
            '2',
            "The policy is the agent's decision-making strategy. It maps every possible state the agent might encounter to the action it should take in that state, and the goal of reinforcement learning is to find the optimal policy."
        ),
        (
            'Reinforcement Learning',
            'What is the exploration versus exploitation trade-off in reinforcement learning?',
            'Choosing between training faster and training more accurately',
            'Balancing trying new actions to discover better strategies against using known good strategies to earn reward',
            'Deciding how much training data to use versus how much to save for testing',
            'Selecting between a simple model and a complex model',
            '2',
            'If an agent only exploits what it already knows, it may miss better strategies. If it only explores, it never makes use of what it has learned. Finding the right balance between the two is one of the central challenges in reinforcement learning.'
        ),
        (
            'Reinforcement Learning',
            'Which of the following is the best real-world application of reinforcement learning?',
            'Classifying customer emails by topic',
            'Training a robot to walk by rewarding successful movements',
            'Translating a document from English to French',
            'Compressing images to reduce file size',
            '2',
            'Teaching a robot to walk is a classic reinforcement learning task. The robot tries different movements and receives rewards when it successfully moves forward without falling, gradually learning a stable walking gait through trial and error.'
        ),

        # Neural Networks
        (
            'Neural Networks',
            'What is a neural network?',
            'A traditional rule-based expert system used in the 1980s',
            'A computational model made of connected nodes in layers that learn to transform data',
            'A type of database optimised for storing numerical data',
            'A programming library used to visualise machine learning results',
            '2',
            'A neural network is a layered system of mathematical nodes called neurons. Data flows through the layers, and the connections between neurons carry weights that are adjusted during training so the network learns to produce correct outputs.'
        ),
        (
            'Neural Networks',
            'What is the purpose of backpropagation?',
            'To shuffle training data before each pass through the network',
            'To calculate how much each weight contributed to the error and adjust all weights accordingly',
            'To add extra layers to a network when it is underfitting',
            "To convert the final layer's output into a probability distribution",
            '2',
            'Backpropagation works by taking the prediction error, tracing it backwards through every layer of the network, and computing how much each weight contributed to that error. The weights are then nudged slightly to reduce the error, and the process repeats.'
        ),
        (
            'Neural Networks',
            'What does a loss function measure during neural network training?',
            'The total number of parameters in the network',
            "How far the model's predictions are from the correct answers",
            'The time taken to complete one training epoch',
            'The proportion of neurons activated in each forward pass',
            '2',
            "The loss function produces a single number that summarises how wrong the model's predictions are compared to the correct answers. Training aims to minimise this number, and gradient descent uses it to work out how to adjust the model's weights."
        ),
        (
            'Neural Networks',
            "What does 'batch size' refer to in neural network training?",
            'The total number of layers in the network architecture',
            'The number of training examples the model processes before updating its weights',
            'The proportion of neurons randomly deactivated by dropout',
            'The learning rate multiplied by the number of epochs',
            '2',
            'Batch size controls how many examples the model looks at before performing one weight update. Larger batches are more stable but slower to compute per update, while smaller batches are noisier but allow more frequent updates.'
        ),
        (
            'Neural Networks',
            'What is an epoch in the context of training a neural network?',
            'One forward pass through a single training example',
            'One complete pass through the entire training dataset',
            'The number of weight updates performed per second',
            'The final evaluation of the model on the test set',
            '2',
            'An epoch is complete when the model has seen every example in the training dataset exactly once. Models typically train for many epochs, repeatedly cycling through the data, until performance on a validation set stops improving.'
        ),

        # Generative AI
        (
            'Generative AI',
            'What is generative AI?',
            'AI that can only classify inputs into predefined categories',
            'AI that creates new content such as text, images, or audio by learning patterns from existing data',
            'AI used exclusively for robotics and physical automation',
            'AI that retrieves and displays information from a fixed database',
            '2',
            'Generative AI models learn the underlying patterns in large amounts of data and then use that knowledge to produce new, original content. Examples include language models that write text and image models that create visuals from descriptions.'
        ),
        (
            'Generative AI',
            'How does a Generative Adversarial Network work?',
            'One network classifies images while another retrieves similar ones from a database',
            'A generator network creates fake outputs while a discriminator network tries to distinguish them from real ones',
            'Two identical networks are trained on different datasets and their outputs are averaged',
            'A single network is trained alternately on positive and negative examples',
            '2',
            'In a GAN, the generator tries to produce outputs convincing enough to fool the discriminator, while the discriminator gets better at spotting fakes. This competition drives both networks to improve, resulting in increasingly realistic generated content.'
        ),
        (
            'Generative AI',
            'What is prompt engineering?',
            'Designing the physical hardware used to run AI models faster',
            'Carefully crafting the text input given to a generative AI model to guide it toward a desired output',
            'Training a model on a new dataset to specialise it for a specific task',
            'Compressing a large AI model so it runs on smaller devices',
            '2',
            "Prompt engineering is the skill of writing instructions or questions for a generative AI in a way that reliably produces useful, accurate, or creative outputs. Small changes in wording can significantly affect the quality of the model's response."
        ),
        (
            'Generative AI',
            'What is an AI hallucination?',
            'When an AI model runs too slowly due to insufficient computing resources',
            'When a generative model produces confident but factually incorrect or made-up information',
            'When a model is biased toward one class in a classification task',
            'When a training run is interrupted before the model fully converges',
            '2',
            'Hallucination refers to the tendency of generative AI models to produce information that sounds plausible and confident but is factually wrong or entirely fabricated. This is a key concern when using AI for tasks where accuracy is critical.'
        ),
        (
            'Generative AI',
            'What type of generative model starts from random noise and progressively refines it into a high-quality image?',
            'Generative Adversarial Network',
            'Recurrent Neural Network',
            'Diffusion model',
            'Decision tree',
            '3',
            'Diffusion models learn to reverse a process of adding random noise to images. At generation time, they start from pure noise and iteratively remove it step by step, guided by a text prompt or other condition, until a coherent image emerges.'
        ),

        # AI Ethics
        (
            'AI Ethics',
            'What is bias in AI?',
            'The tendency of a model to train faster on some examples than others',
            'When a model produces systematically unfair or skewed results due to imbalanced or unrepresentative training data',
            'The amount of memory a model uses during inference',
            "The difference between a model's training accuracy and test accuracy",
            '2',
            'AI bias occurs when training data does not equally represent all groups or reflects existing societal inequalities, causing the model to produce outcomes that are systematically unfair to particular people. It is one of the most important problems in responsible AI development.'
        ),
        (
            'AI Ethics',
            'Why is explainability important in AI systems?',
            'It makes models run faster on low-powered devices',
            "It allows people to understand and trust the reasoning behind a model's decisions, especially in high-stakes situations",
            'It reduces the amount of labelled data needed to train a model',
            'It automatically corrects any errors the model makes during inference',
            '2',
            'When AI makes decisions about loans, medical diagnoses, or legal outcomes, people have a right to understand why. Explainability allows developers to spot errors and biases, and it gives affected individuals a meaningful way to question or appeal decisions.'
        ),
        (
            'AI Ethics',
            'What does fairness in AI mean?',
            'Making sure all models are trained on the same dataset',
            "Ensuring that a model's outputs do not systematically disadvantage groups based on attributes like race or gender",
            "Balancing the model's precision and recall equally",
            'Giving all training examples the same weight during optimisation',
            '2',
            'Fairness in AI means that the model should not produce outcomes that discriminate against people based on protected characteristics. Achieving fairness often requires careful dataset curation, auditing of model outputs, and sometimes deliberately adjusting how the model is trained.'
        ),
        (
            'AI Ethics',
            'What is the concept of AI alignment concerned with?',
            'Connecting multiple AI systems so they can share data',
            "Ensuring that an AI system's goals and behaviours remain in line with human intentions and values",
            "Aligning the training data columns with the model's expected input format",
            'Making sure AI systems run at consistent speeds across different hardware',
            '2',
            'AI alignment is about making sure that as AI systems become more powerful and autonomous, they continue to pursue goals that are genuinely beneficial to humans rather than drifting toward objectives that could cause harm, even unintentionally.'
        ),
        (
            'AI Ethics',
            'What does privacy in AI primarily refer to?',
            "Keeping the model's architecture secret from competitors",
            "Ensuring AI systems collect, use, and protect personal data in ways that respect individuals' rights",
            "Preventing users from seeing the model's confidence scores",
            'Encrypting the model weights so they cannot be copied',
            '2',
            'Privacy in AI is about how personal data is handled throughout the lifecycle of an AI system. This includes minimising data collection, anonymising what is collected, securing it from breaches, and giving individuals meaningful control over their own information.'
        ),

        # Large Language Models
        (
            'Large Language Models',
            'What is a Large Language Model?',
            'A traditional search engine that indexes web pages',
            'An AI system trained on vast amounts of text to understand and generate human-like language',
            'A specialised database designed to store and retrieve documents quickly',
            'A type of computer chip optimised for running neural network calculations',
            '2',
            'Large Language Models are trained on enormous text datasets and learn to predict and generate language. This training allows them to answer questions, write code, summarise documents, translate languages, and hold coherent conversations across a huge range of topics.'
        ),
        (
            'Large Language Models',
            'What is the Transformer architecture?',
            'A hardware component that converts power for AI accelerators',
            'The neural network design that uses attention to relate all parts of an input sequence to each other simultaneously',
            'A training algorithm that replaces gradient descent for large models',
            'A data compression technique for reducing the size of language model outputs',
            '2',
            'The Transformer, introduced in 2017, is the architecture behind nearly all modern large language models. Its key innovation is the attention mechanism, which allows the model to consider the relationship between every token and every other token in the input at once.'
        ),
        (
            'Large Language Models',
            'What does fine-tuning a language model involve?',
            'Removing parameters from the model to make it run faster',
            'Continuing to train a pre-trained model on a smaller, task-specific dataset to specialise its behaviour',
            'Restarting training from scratch with a different random seed',
            "Translating the model's weights into a different numerical format",
            '2',
            'Fine-tuning takes a large pre-trained model that already has broad language knowledge and adapts it to a specific domain or task by training it further on relevant examples. This is far more efficient than training a specialist model from scratch.'
        ),
        (
            'Large Language Models',
            'What problem does Retrieval-Augmented Generation solve?',
            'It reduces the number of parameters needed to run a large language model',
            'It allows a language model to access up-to-date or domain-specific facts by searching external sources before responding',
            'It speeds up the tokenisation step in natural language processing pipelines',
            'It prevents language models from generating text that is too long',
            '2',
            'Language models have a fixed knowledge cutoff and can hallucinate facts. RAG addresses this by connecting the model to a search system so it can retrieve relevant, accurate, up-to-date information before composing its response.'
        ),
        (
            'Large Language Models',
            'What does the attention mechanism in a Transformer model allow it to do?',
            'Process only the most recent token without considering previous ones',
            'Weigh the importance of different parts of the input relative to each other when producing each output token',
            'Store information in an external memory bank between conversations',
            'Convert numerical embeddings back into readable text',
            '2',
            'Attention allows the model to dynamically focus on the most relevant parts of the input for each step of its output. When translating a sentence, for example, the model can attend strongly to the words most relevant to the current word it is generating.'
        ),
    ]

    
    cursor.executemany(
        'INSERT INTO definitions (topic, definition, example) VALUES (?, ?, ?)',
        definitions_data
    )

    cursor.executemany(
        'INSERT INTO funfacts (topic, fun_fact) VALUES (?, ?)',
        funfacts_data
    )

    cursor.executemany(
        'INSERT INTO quiz_questions (topic, question, option_1, option_2, option_3, option_4, answer, explanation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        quiz_data
    )

    conn.commit()
    conn.close()

    print(f"Database initialised: {DB_NAME}")
    print(f"  definitions   : {len(definitions_data)} rows")
    print(f"  funfacts      : {len(funfacts_data)} rows")
    print(f"  quiz_questions: {len(quiz_data)} rows")


if __name__ == '__main__':
    setup_database()