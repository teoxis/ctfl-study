from qlib_ai import q

# ---------------- AI-1.1.1 (K2) AI-based vs conventional systems ----------------
q("1.1.1", "Which statement BEST describes how most ML-based systems differ from conventional systems in the way they produce outputs?",
  "They derive their behavior from patterns learned from data instead of following explicitly programmed rules",
  ["They are programmed with more detailed if-then-else rules than conventional systems",
   "They always produce the same output for the same input, which makes them easier to test",
   "They do not need any data once the developers have written the algorithm"],
  "La diferencia clave (1.1.1): los sistemas convencionales siguen reglas escritas paso a paso; los basados en ML aprenden patrones de los datos. Precisamente por eso no siempre son deterministas ni fáciles de explicar.")
q("1.1.1", "Why is explainability a particular challenge for many AI-based systems?",
  "Models such as deep neural networks can have billions of parameters, so humans cannot easily follow how an input led to an output",
  ["AI-based systems are written in programming languages that testers cannot read",
   "AI-based systems hide their outputs from users for security reasons",
   "Explainability only matters for conventional systems, because AI-based systems are self-documenting"],
  "El syllabus describe la naturaleza de \"caja negra\": con miles de millones de parámetros, no se puede seguir el razonamiento interno. En sanidad, finanzas, defensa o transporte es crítico saber por qué se tomó una decisión.")
q("1.1.1", "A team replaces a hand-coded spam filter with a self-learning ML model that keeps updating itself from new emails. What additional need does this adaptability create?",
  "Continuous monitoring to check that the system stays aligned with its core requirements",
  ["Rewriting the if-then-else rules every time a new email arrives",
   "Removing all test cases, because self-learning systems test themselves",
   "Freezing the input data so that the model never sees new emails"],
  "La adaptabilidad es una ventaja en entornos cambiantes, pero el syllabus advierte que exige monitorización continua para que el sistema siga cumpliendo sus requisitos (puede \"aprender\" algo indeseado).")
q("1.1.1", "Which characteristic is MOST typical of a conventional (non-AI) system?",
  "Its behavior is deterministic and transparent: developers can trace how each input produces its output",
  ["It handles ambiguity through probabilistic reasoning",
   "It improves its own performance as it encounters new data",
   "Its internal logic is learned from labeled examples"],
  "Los sistemas convencionales se programan de forma imperativa (bucles, if-then-else): son deterministas y transparentes. Razonamiento probabilístico, autoaprendizaje y lógica aprendida son rasgos de los sistemas de IA.")
q("1.1.1", "Many AI-based systems rely on probabilistic reasoning and statistical inference. What is a direct consequence for testing?",
  "Their outputs are not always predictable, so exact expected results are harder to define",
  ["Their outputs are always wrong a fixed percentage of the time",
   "They cannot be tested at all and must be accepted as they are",
   "They become fully deterministic once deployed to production"],
  "Al basarse en razonamiento probabilístico, manejan mejor la incertidumbre pero sus salidas no siempre son predecibles. Esto complica definir un resultado esperado exacto (el problema del oráculo, que se ve en el capítulo 4).")
q("1.1.1", "An image recognition system identifies cats in photos. How did it MOST likely acquire this ability?",
  "It was trained on a dataset of cat images and extracts patterns that it applies to new, unseen images",
  ["A developer coded rules such as 'if it has whiskers and pointed ears, it is a cat'",
   "It searches the internet for each photo and copies the most common caption",
   "It compares each photo pixel by pixel with a single reference photo of a cat"],
  "Es el ejemplo del propio syllabus: el sistema no usa reglas codificadas, sino que aprende de un dataset de imágenes de gatos y aplica esos patrones a imágenes que nunca ha visto.")

# ---------------- AI-1.1.2 (K2) Narrow, general and super AI ----------------
q("1.1.2", "Which statement about narrow AI is correct?",
  "All AI-based systems deployed today are narrow AI, and they cannot generalize beyond the tasks they have learned",
  ["Narrow AI can perform most intellectual tasks that a human can",
   "Narrow AI improves itself continuously without any human intervention",
   "Narrow AI is a theoretical concept that has not been achieved yet"],
  "La IA estrecha (débil) es toda la IA desplegada hoy: muy eficaz en su dominio, pero sin capacidad de generalizar. Hacer casi cualquier tarea humana sería IA general; mejorarse sin control humano, superinteligencia.")
q("1.1.2", "A face recognition system performs excellently. The company now wants it to translate documents. According to the syllabus, what would be needed?",
  "Explicitly retraining it for translation, because narrow AI cannot transfer its skill to a different task",
  ["Nothing, because a system that excels at one task can perform any other task",
   "Connecting it to the internet so that it can learn translation on its own",
   "Upgrading it to super AI by adding more GPUs"],
  "Es el ejemplo del syllabus: un sistema de IA estrecha que reconoce caras no puede traducir salvo que se reentrene explícitamente para ello.")
q("1.1.2", "How does the syllabus position frontier AI?",
  "As a subset of narrow AI: the most advanced current systems, still task-specific and not general AI",
  ["As the first achieved form of general AI",
   "As a synonym for super AI",
   "As a category of conventional rule-based systems"],
  "La IA de frontera (los modelos generativos más avanzados) es un subconjunto de la IA estrecha: muy capaz y autónoma, pero sigue siendo específica de tareas y no alcanza la versatilidad de la IA general.")
q("1.1.2", "Which description matches general AI (strong AI)?",
  "A system that could understand, learn and apply knowledge across most intellectual tasks a human can, without retraining for each task",
  ["A system specialized in one domain, such as speech recognition",
   "A system that improves itself without human control and surpasses human intelligence",
   "A system built from explicit if-then-else rules written by experts"],
  "IA general = capacidad humana en casi cualquier tarea intelectual, sin reentrenar para cada una. El syllabus subraya que ningún sistema actual la posee. Superar a los humanos y automejorarse sería superinteligencia.")
q("1.1.2", "What is the technological singularity?",
  "The point at which AI-based systems would transition from general AI to super AI, if it ever occurred",
  ["The moment a narrow AI system is deployed to production for the first time",
   "The point at which a neural network reaches one billion parameters",
   "The release date of the first large language model"],
  "El syllabus define la singularidad tecnológica como el punto de transición de la IA general a la superinteligencia, si llegara a ocurrir.")
q("1.1.2", "Which statement about super AI is consistent with the syllabus?",
  "It would continuously improve itself without human intervention, and internet access is not strictly required although it could expand its capabilities",
  ["It already exists in today's frontier models",
   "It cannot exist without permanent access to the internet",
   "It is another name for narrow AI used in safety-critical systems"],
  "Superinteligencia: se automejora sin intervención humana y superaría la inteligencia humana. El syllabus precisa que el acceso a internet no es estrictamente necesario, aunque ampliaría mucho su capacidad e influencia.")

# ---------------- AI-1.1.3 (K2) Types of AI technologies ----------------
q("1.1.3", "Which statement BEST describes the relationship between AI, ML and deep learning?",
  "ML is one branch of AI, and deep learning is a subset of ML methods that uses deep neural networks",
  ["Deep learning is the broadest field, and AI is one of its techniques",
   "ML and deep learning are unrelated fields that both compete with AI",
   "AI is a subset of ML that only covers rule-based systems"],
  "Jerarquía: IA ⊃ ML ⊃ deep learning. El ML aprende de los datos sin programación explícita; el DL es un subconjunto del ML basado en redes neuronales profundas.")
q("1.1.3", "A team has thousands of customer records without any labels and wants to discover groups of similar customers. Which approach fits BEST?",
  "Unsupervised learning, for example a clustering algorithm",
  ["Supervised learning with linear regression",
   "Reinforcement learning with a reward signal",
   "A rule-based expert system"],
  "Datos sin etiquetar + descubrir patrones (grupos) = aprendizaje no supervisado (clustering). El supervisado necesita datos etiquetados; el de refuerzo aprende por prueba y error con su entorno.")
q("1.1.3", "Which deep learning architecture is particularly effective for image recognition and object detection?",
  "Convolutional neural networks (CNN)",
  ["Recurrent neural networks (RNN)",
   "Bayesian models",
   "Fuzzy logic"],
  "Según el syllabus: CNN para imágenes y detección de objetos; RNN para datos secuenciales (texto, series temporales); transformers para dependencias de largo alcance (LLM).")
q("1.1.3", "An agent learns to play a game by trying moves and receiving points for good outcomes. Which form of ML is this?",
  "Reinforcement learning",
  ["Supervised learning",
   "Unsupervised learning",
   "Rule-based reasoning"],
  "Aprendizaje por refuerzo: un agente aprende el comportamiento óptimo por prueba y error interactuando con su entorno y recibiendo recompensas.")
q("1.1.3", "Which AI technology is designed for reasoning under uncertainty, for example with degrees of truth instead of strict true/false values?",
  "Fuzzy logic",
  ["Search algorithms",
   "Computer vision",
   "Convolutional neural networks"],
  "El syllabus cita la lógica difusa para razonar con incertidumbre; los algoritmos de búsqueda, para optimización (navegación, decisiones estratégicas); la visión por computador, para datos visuales.")
q("1.1.3", "What distinguishes agentic AI, as described in the syllabus?",
  "Autonomous agents that plan, reason and act independently to achieve goals in dynamic environments",
  ["Systems that only classify inputs into fixed categories",
   "Expert systems that follow rules written by domain specialists",
   "Models that generate images by adding and removing noise"],
  "La IA agéntica extiende estas tecnologías con agentes autónomos que planifican, razonan y actúan por sí mismos para lograr objetivos. Es lo que hace un agente de programación como Claude Code u opencode.")

# ---------------- AI-1.1.4 (K2) Generative AI ----------------
q("1.1.4", "Which statement BEST describes generative AI?",
  "AI-based systems that create new content such as text, images, audio or video, learned from large amounts of training data",
  ["Systems that only sort existing data into predefined categories",
   "Rule-based systems that generate reports from database queries",
   "Systems that compress existing files to save storage space"],
  "La IA generativa crea contenido nuevo (texto, imágenes, vídeo, música, datos complejos) parecido a sus datos de entrenamiento. Muchos sistemas también clasifican o predicen, pero lo que la define es generar.")
q("1.1.4", "Which technology behind generative AI uses two neural networks competing against each other to produce realistic synthetic data?",
  "Generative adversarial networks (GANs)",
  ["Diffusion models",
   "Transformers",
   "Decision trees"],
  "Las GAN enfrentan dos redes (una genera, otra juzga). Los modelos de difusión añaden y quitan ruido gradualmente; los transformers usan autoatención y son la base de los LLM.")
q("1.1.4", "What mechanism do transformer models, which underpin LLMs, use to generate coherent and contextually relevant text?",
  "Self-attention",
  ["Adding and then removing noise from the data",
   "Two competing networks, a generator and a discriminator",
   "Explicit grammar rules written by linguists"],
  "Los transformers usan mecanismos de autoatención (self-attention) para relacionar cada parte del texto con el resto del contexto. Añadir/quitar ruido es difusión; generador contra discriminador es una GAN.")
q("1.1.4", "Which of the following is a societal or ethical concern of generative AI listed in the syllabus?",
  "Misuse to create deepfakes, spread misinformation or generate convincing fraudulent content",
  ["GenAI systems cannot produce content in more than one language",
   "GenAI systems require no computational resources once trained",
   "GenAI has no effect on employment because it only automates manual labor"],
  "El syllabus cita el mal uso (deepfakes, desinformación, fraude), el impacto en el empleo de profesiones de oficina, y la sostenibilidad (alto consumo de energía y huella de carbono).")
q("1.1.4", "Most practical GenAI tools today are built in which way?",
  "On foundation models that are then fine-tuned for specific applications",
  ["Entirely from scratch for each application, without pretrained models",
   "As rule-based expert systems with hand-written knowledge bases",
   "On small decision trees trained on a single spreadsheet"],
  "La mayoría de herramientas de GenAI parten de modelos fundacionales que luego se ajustan (fine-tuning) para aplicaciones concretas. El campo avanza hacia modelos multimodales (texto, imagen, audio).")
q("1.1.4", "Why does the syllabus raise sustainability as an issue for generative AI?",
  "Training and running large GenAI models need substantial computational resources, leading to high energy consumption and a significant carbon footprint",
  ["GenAI models produce physical waste when they generate images",
   "GenAI models can only run on hardware that cannot be recycled",
   "GenAI models stop working after a fixed number of uses"],
  "Entrenar y ejecutar modelos grandes consume muchísima computación, con alto consumo energético y huella de carbono. Por eso se piden diseños más eficientes e infraestructura más verde.")

# ---------------- AI-1.1.5 (K2) Hardware for ML ----------------
q("1.1.5", "Why do GPUs typically outperform CPUs for machine learning, even though CPUs usually run at higher clock speeds?",
  "GPUs have thousands of cores designed for massively parallel, relatively simple operations such as matrix multiplication",
  ["GPUs perform complex high-precision operations that ML always requires",
   "CPUs cannot store the data structures used by ML models",
   "GPUs are the only hardware that can run neural networks at all"],
  "El ML se beneficia del procesamiento masivamente paralelo (multiplicación de matrices). Las GPU tienen miles de núcleos para operaciones simples en paralelo; las CPU tienen pocos núcleos y una precisión que el ML no suele necesitar.")
q("1.1.5", "A model's weights are converted from 32-bit to 4-bit numbers. Which benefit does the syllabus associate with this low-precision arithmetic (quantization)?",
  "Faster processing, lower power consumption, smaller and cheaper chips, and reduced bandwidth requirements",
  ["Higher precision in every calculation the model performs",
   "Elimination of the need for training data",
   "Guaranteed identical outputs to the 32-bit model in every case"],
  "La cuantización usa menos bits por número: más velocidad, menos consumo, chips más pequeños y baratos, y menos ancho de banda. Es lo que haces al usar un modelo Q4 en llama.cpp. No garantiza salidas idénticas: algo de precisión se pierde.")
q("1.1.5", "A speech recognition model must run on low-end smartphones. Where would it MOST likely be trained?",
  "In the cloud, using powerful hardware, while inference runs on the phone",
  ["On the same low-end smartphone, because training and inference always use the same hardware",
   "On a single CPU core, because training needs less power than inference",
   "Nowhere, because speech recognition models do not need training"],
  "Es el ejemplo del syllabus: entrenamiento e inferencia pueden usar hardware distinto. Un modelo puede ejecutarse en un móvil sencillo aunque necesite la potencia de la nube para entrenarse.")
q("1.1.5", "For which use are AI-specific chips such as ASICs and System-on-a-Chip devices BEST suited, according to the syllabus?",
  "Edge computing, with the training of the model performed in the cloud on specialized hardware",
  ["Training very large models from scratch on a single device",
   "Running general-purpose office software",
   "Replacing GPUs in all data centers"],
  "Los chips específicos de IA (ASIC, SoC) tienen varios núcleos, gestión de datos especializada y procesamiento en memoria; son ideales para edge computing, mientras el entrenamiento se hace en la nube.")
q("1.1.5", "What is characteristic of neuromorphic processors?",
  "They do not use the traditional von Neumann architecture but brain-inspired designs that mimic neuronal structures",
  ["They are standard CPUs with a higher clock speed",
   "They are GPUs optimized for graphics rendering",
   "They are designed specifically to run on the von Neumann architecture"],
  "Los procesadores neuromórficos abandonan la arquitectura von Neumann y usan diseños inspirados en el cerebro que imitan estructuras neuronales.")
q("1.1.5", "Which hardware capability does ML typically benefit from, according to the syllabus?",
  "The ability to work with large data structures",
  ["Very high clock speeds on a few cores",
   "High-precision arithmetic for every operation",
   "Sequential processing of one instruction at a time"],
  "El ML se beneficia de: trabajar con estructuras de datos grandes, procesamiento masivamente paralelo y aritmética de baja precisión. Pocos núcleos rápidos y alta precisión son rasgos de las CPU, menos adecuados.")

# ---------------- AI-1.1.6 (K2) Development and hosting ----------------
q("1.1.6", "A bank must keep its customer data private but needs a lot of computing power to train models. Which approach does the syllabus describe as common for such cases?",
  "A hybrid approach: prepare the sensitive data on-premises and use cloud resources for the compute-intensive tasks",
  ["Upload all customer data to a public cloud, because public clouds are always the most secure option",
   "Train everything on employees' personal computers",
   "Avoid AI entirely, because private data can never be used for training"],
  "Muchas organizaciones adoptan enfoques híbridos: prototipos en local, componentes sensibles (como la preparación de datos privados) on-premises y la nube para lo que necesita mucha computación.")
q("1.1.6", "What is a typical advantage of acquiring a third-party pretrained model or AI as a Service (AIaaS) instead of developing a private model?",
  "Faster deployment and quicker time-to-market",
  ["Full control over every internal detail of the model",
   "No dependency on any external provider",
   "Guaranteed compliance with all regulations without testing"],
  "Los sistemas de terceros (modelos preentrenados o AIaaS) permiten desplegar antes. Los privados se adaptan mejor a requisitos específicos, pero exigen habilidades especializadas.")
q("1.1.6", "Which statement about hosting AI models locally on personal computers or smartphones is correct?",
  "It offers privacy and avoids cloud licensing costs, but hardware capabilities are limited",
  ["It provides unlimited scalability for fluctuating workloads",
   "It is only possible for the largest models",
   "It removes the need to consider model size"],
  "El alojamiento local da privacidad y elimina licencias de nube, a cambio de hardware limitado: sirve para modelos pequeños. Es exactamente tu agente local en el MacBook.")
q("1.1.6", "What is a typical benefit of developing AI models in a public cloud?",
  "Pre-configured environments with pay-as-you-go pricing that limit the initial hardware investment and scale easily",
  ["Maximum control and privacy for highly sensitive data",
   "No running costs once the account is created",
   "The ability to train any model without data"],
  "La nube pública ofrece entornos preconfigurados y pago por uso: poca inversión inicial y fácil escalado. Más control y privacidad da la nube privada, con más inversión inicial.")
q("1.1.6", "Which factor does the syllabus list as influencing the choice of development and hosting solutions?",
  "Security and data privacy considerations",
  ["The color scheme of the user interface",
   "The number of testers on the team",
   "The programming language used for the company website"],
  "Factores citados: tamaño y complejidad del modelo, requisitos de rendimiento, presupuesto, seguridad y privacidad de datos, necesidades de despliegue y requisitos regulatorios. Desarrollo y alojamiento suelen decidirse por separado.")
q("1.1.6", "A start-up wants to train a mid-sized model locally. What does the syllabus say such models may require?",
  "Dedicated GPUs, while small models can be developed on personal computers and large ones need on-premises server clusters",
  ["Nothing beyond a standard smartphone",
   "A neuromorphic processor in every case",
   "A public cloud account, because local development of mid-sized models is impossible"],
  "Escala según el syllabus: modelos pequeños (árboles de decisión, redes compactas) en un PC; medianos, GPU dedicadas; grandes, clústeres de servidores on-premises con sus costes de energía, refrigeración y hardware.")

# ---------------- AI-1.1.7 (K2) ML development frameworks ----------------
q("1.1.7", "Which functionality do ML development frameworks typically provide?",
  "Data handling, model building, training and optimization, evaluation and, in some cases, deployment",
  ["Only a graphical interface for drawing neural network diagrams",
   "Only hosting services for finished models",
   "Only legal checks for regulatory compliance"],
  "Funciones típicas (1.1.7): manejo de datos, construcción del modelo, entrenamiento y optimización, evaluación y, en algunos, despliegue.")
q("1.1.7", "In an ML framework, which functionality iteratively adjusts the model's internal parameters based on the training data and the desired result?",
  "Training and optimization",
  ["Data handling",
   "Deployment",
   "Evaluation"],
  "Entrenamiento y optimización: algoritmos que ajustan iterativamente los parámetros internos para optimizar el rendimiento en la tarea (clasificación, regresión…).")
q("1.1.7", "A framework converts a trained model into a format that can run inside a mobile app. Which functionality is this?",
  "Deployment",
  ["Model building",
   "Data handling",
   "Training and optimization"],
  "Despliegue: convertir el modelo entrenado a un formato integrable en aplicaciones web, móviles, dispositivos edge o sistemas embebidos.")
q("1.1.7", "What is the trade-off between frameworks offering a lower-level API and those offering a higher-level API?",
  "A lower-level API gives more control over model building but requires more coding expertise; a higher-level API simplifies creation but allows less customization",
  ["A lower-level API is always faster to learn and offers more control",
   "A higher-level API always produces more accurate models",
   "There is no difference: the level of the API only changes the documentation"],
  "Bajo nivel = más control, más código y experiencia necesarios. Alto nivel = más sencillo, menos personalización.")
q("1.1.7", "Which of the following is a factor for selecting an ML framework, according to the syllabus?",
  "The level of community support and the maturity of the ecosystem",
  ["The age of the framework's logo",
   "Whether the framework was created in the same country as the project",
   "The number of letters in the framework's name"],
  "Factores: área de aplicación, interfaz amigable para prototipos rápidos, configurabilidad para modelos complejos, experiencia de los usuarios, consideraciones de despliegue, nivel de soporte (de la comunidad) y madurez del ecosistema.")
q("1.1.7", "Which functionality of an ML framework measures accuracy, precision and recall on unseen data?",
  "Evaluation",
  ["Data handling",
   "Model building",
   "Deployment"],
  "Evaluación: medir cómo de bien funciona el modelo con datos no vistos (exactitud, precisión y recall en clasificación; tasas de error en regresión).")

# ---------------- AI-1.1.8 (K2) Regulations and standards ----------------
q("1.1.8", "How does the EU AI Act regulate AI-based systems?",
  "With a risk-based approach that categorizes systems from minimal to unacceptable risk, with stringent requirements for high-risk systems",
  ["With a single set of identical rules for every AI-based system",
   "By banning all AI-based systems used in healthcare and finance",
   "Through voluntary guidelines without any penalties"],
  "La EU AI Act clasifica por riesgo (de mínimo a inaceptable). Los sistemas de alto riesgo afrontan requisitos estrictos: pruebas rigurosas, gobernanza de datos y supervisión humana; las multas se calculan sobre la facturación global.")
q("1.1.8", "Which of the following are described in the syllabus as influential soft law instruments for responsible AI?",
  "The OECD AI Principles and the UN report on Governing AI for Humanity",
  ["The EU AI Act and national criminal codes",
   "ISO/IEC TR 29119-11 and the ISO/IEC 42119 series",
   "Company-internal coding guidelines"],
  "Soft law (no vinculante): los Principios de IA de la OCDE y el informe de la ONU *Governing AI for Humanity*. La EU AI Act es regulación vinculante; las normas ISO/IEC son estándares técnicos.")
q("1.1.8", "Which standard provides detailed guidance on testing AI-based systems?",
  "ISO/IEC TR 29119-11",
  ["The OECD AI Principles",
   "The EU AI Act",
   "The UN report on Governing AI for Humanity"],
  "ISO/IEC TR 29119-11 da guía detallada para probar sistemas de IA, clave para demostrar cumplimiento normativo. Además, la serie ISO/IEC 42119 está en desarrollo para cubrir distintos aspectos de la prueba de IA.")
q("1.1.8", "What role do technical standards from organizations such as ISO and IEEE play in AI governance?",
  "They translate high-level aspirations into concrete technical specifications and best practices, bridging policy and practice",
  ["They replace national laws on AI",
   "They only define marketing terminology for AI products",
   "They set the financial penalties for non-compliance"],
  "Los estándares técnicos convierten los principios de alto nivel en especificaciones y buenas prácticas concretas: el puente entre la política y la práctica.")
q("1.1.8", "According to the syllabus, what do high-risk AI-based systems face under the EU AI Act?",
  "Stringent requirements including rigorous testing, data governance and human oversight",
  ["No requirements, as long as they are developed in the EU",
   "Only a requirement to publish their source code",
   "An automatic ban, regardless of their purpose"],
  "Alto riesgo (los que afectan a derechos fundamentales o a la seguridad) = pruebas rigurosas, gobernanza de datos y supervisión humana. Para un tester esto significa que la prueba es una obligación legal, no solo una buena práctica.")
q("1.1.8", "How does the syllabus contrast the EU's approach to AI regulation with that of many nations outside the EU?",
  "Many nations outside the EU are adopting a more permissive, lighter-touch approach to encourage innovation",
  ["Nations outside the EU have banned AI completely",
   "All nations have adopted the EU AI Act unchanged",
   "Nations outside the EU regulate only conventional systems, not AI"],
  "Frente al enfoque estricto y basado en riesgo de la UE, muchos países fuera de ella optan por regulaciones más ligeras para fomentar la innovación. El syllabus también señala regulación sectorial emergente en sanidad y finanzas.")
