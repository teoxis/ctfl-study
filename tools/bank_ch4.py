from qlib import q

# ---------------- FL-4.1.1 (K2) Black-box / white-box / experience-based (10) ----------------
q("4.1.1", "Which statement about black-box test techniques is correct?",
  "Test cases are independent of how the software is implemented, so they remain useful if the implementation changes but the required behavior stays the same",
  ["Test cases can only be created after the code is written",
   "Test cases are based on the internal structure of the test object",
   "Their effectiveness depends mainly on the tester's experience"],
  "Las técnicas de caja negra (basadas en la especificación) analizan el comportamiento especificado sin mirar la estructura interna; por eso sus casos siguen valiendo si cambia la implementación.")
q("4.1.1", "Why can white-box test cases only be created after the design or implementation of the test object?",
  "Because they depend on how the software is designed, i.e., on its internal structure and processing",
  ["Because they are derived from user stories",
   "Because they require experienced testers",
   "Because they are always automated"],
  "Las técnicas de caja blanca (basadas en la estructura) analizan la estructura interna, así que necesitan el diseño o la implementación.")
q("4.1.1", "Which statement about experience-based test techniques is correct?",
  "They can detect defects that may be missed by black-box and white-box techniques, so they are complementary to them",
  ["They replace black-box and white-box techniques",
   "Their effectiveness does not depend on the tester's skills",
   "They are based on the analysis of the code structure"],
  "Las técnicas basadas en la experiencia aprovechan el conocimiento del tester; su eficacia depende mucho de sus habilidades y complementan a las de caja negra y blanca.")
q("4.1.1", "Black-box test techniques are also known as:",
  "Specification-based techniques",
  ["Structure-based techniques",
   "Experience-based techniques",
   "Collaboration-based techniques"],
  "Caja negra = basadas en la especificación; caja blanca = basadas en la estructura.")
q("4.1.1", "White-box test techniques are also known as:",
  "Structure-based techniques",
  ["Specification-based techniques",
   "Risk-based techniques",
   "Checklist-based techniques"],
  "Las técnicas de caja blanca también se llaman basadas en la estructura.")
q("4.1.1", "In which test activities do test techniques support the tester?",
  "Test analysis (what to test) and test design (how to test)",
  ["Only test execution",
   "Only test completion",
   "Only test monitoring and control"],
  "Las técnicas apoyan el análisis (qué probar) y el diseño (cómo probar): ayudan a definir condiciones, identificar elementos de cobertura y datos de prueba.")
q("4.1.1", "Which technique category is being used when a tester derives test cases by analysing the branches of the source code?",
  "White-box test technique",
  ["Black-box test technique",
   "Experience-based test technique",
   "Collaboration-based test approach"],
  "Analizar las ramas del código es una técnica de caja blanca (prueba de ramas).")
q("4.1.1", "Which technique category is being used when a tester derives test cases from equivalence partitions defined in the requirements?",
  "Black-box test technique",
  ["White-box test technique",
   "Experience-based test technique",
   "Static analysis"],
  "La partición de equivalencia aplicada a requisitos especificados es una técnica de caja negra.")
q("4.1.1", "Which technique category is being used when a tester anticipates defects based on failures seen in similar applications?",
  "Experience-based test technique",
  ["Black-box test technique",
   "White-box test technique",
   "Collaboration-based test approach"],
  "Anticipar defectos a partir de la experiencia (error guessing) es una técnica basada en la experiencia.")
q("4.1.1", "What is the main purpose of using test techniques?",
  "To develop a relatively small, but sufficient, set of test cases in a systematic way",
  ["To achieve exhaustive testing",
   "To replace test planning",
   "To guarantee that all defects are found"],
  "Las técnicas ayudan a obtener de forma sistemática un conjunto de casos relativamente pequeño pero suficiente.")

# ---------------- FL-4.3.1 (K2) Statement testing (7) ----------------
q("4.3.1", "In statement testing, what are the coverage items?",
  "Executable statements",
  ["Branches",
   "Equivalence partitions",
   "Decision rules"],
  "En la prueba de sentencias los elementos de cobertura son las sentencias ejecutables.")
q("4.3.1", "How is statement coverage measured?",
  "Number of statements exercised by the test cases divided by the total number of executable statements, as a percentage",
  ["Number of branches exercised divided by the total number of branches",
   "Number of test cases passed divided by the number of test cases run",
   "Number of lines of code divided by the number of test cases"],
  "Cobertura de sentencias = sentencias ejercitadas / sentencias ejecutables totales, en porcentaje.")
q("4.3.1", "Which statement about 100% statement coverage is correct?",
  "It ensures every executable statement has been exercised at least once, but it may not detect data-dependent defects such as division by zero",
  ["It guarantees that all branches have been exercised",
   "It guarantees that the code is defect-free",
   "It ensures that all paths through the code have been tested"],
  "El 100 % de sentencias garantiza ejecutar cada sentencia, pero no detecta todos los defectos (p. ej., dependientes de datos) ni garantiza ejercitar todas las ramas.")
q("4.3.1", "Why might 100% statement coverage NOT ensure that all the decision logic has been tested?",
  "Because it may not exercise all the branches in the code, e.g., the false outcome of an IF without ELSE",
  ["Because statement coverage counts only comments",
   "Because statement coverage requires every path to be executed",
   "Because statement coverage is a black-box measure"],
  "Un IF sin ELSE puede cubrirse con la salida verdadera ejecutando todas las sentencias, sin probar nunca la salida falsa.")
q("4.3.1", "Consider the code below. What is the minimum number of test cases needed to achieve 100% statement coverage?",
  "1",
  ["2", "3", "4"],
  "Un único test con a = 11 y b = 6 ejecuta todas las sentencias (las dos condiciones son verdaderas). La cobertura de sentencias no exige probar las salidas falsas.",
  code="IF a > 10 THEN\n    x = 1\nENDIF\nIF b > 5 THEN\n    y = 2\nENDIF")
q("4.3.1", "What is the main benefit of achieving 100% statement coverage?",
  "Each statement containing a defect will be executed, which may cause a failure that demonstrates the defect",
  ["All requirements are guaranteed to be implemented",
   "All combinations of inputs have been tested",
   "No regression testing is needed afterwards"],
  "El syllabus indica que, con el 100 %, cada sentencia con un defecto se ejecuta, lo que puede provocar un fallo que demuestre su presencia.")
q("4.3.1", "A program has 40 executable statements. The tests exercise 30 of them. What is the statement coverage?",
  "75%",
  ["70%", "30%", "80%"],
  "Cobertura = 30 / 40 = 75 %.")

# ---------------- FL-4.3.2 (K2) Branch testing (7) ----------------
q("4.3.2", "Which statement about statement coverage and branch coverage is correct?",
  "Branch coverage subsumes statement coverage: 100% branch coverage achieves 100% statement coverage, but not vice versa",
  ["100% statement coverage guarantees 100% branch coverage",
   "Both always require the same number of test cases",
   "Branch coverage is a black-box coverage measure"],
  "Cualquier conjunto que logre el 100 % de ramas logra el 100 % de sentencias, pero no al revés.")
q("4.3.2", "What is a branch, according to the syllabus?",
  "A transfer of control between two nodes in the control flow graph, either unconditional or conditional",
  ["A single executable statement",
   "A path from the start to the end of the program",
   "A combination of conditions in a decision table"],
  "Una rama es una transferencia de control entre dos nodos del grafo de flujo de control; puede ser incondicional (código lineal) o condicional (resultado de una decisión).")
q("4.3.2", "For the code below, what is the minimum number of test cases needed to achieve 100% branch coverage?",
  "2",
  ["1", "3", "4"],
  "Hay que recorrer las salidas verdadera y falsa de las dos decisiones. Un test con ambas verdaderas y otro con ambas falsas lo consiguen: 2 tests.",
  code="IF a > 10 THEN\n    x = 1\nENDIF\nIF b > 5 THEN\n    y = 2\nENDIF")
q("4.3.2", "Which of the following corresponds to conditional branches?",
  "The outcomes of an IF decision, the outcomes of a switch/case statement, and the decision to exit or continue a loop",
  ["Only the lines of code inside a function",
   "Only unconditional jumps",
   "Only the comments in the code"],
  "Las ramas condicionales corresponden a los resultados verdadero/falso de un IF, a las salidas de un switch/case o a la decisión de salir o continuar un bucle.")
q("4.3.2", "Which defect might NOT be detected even with 100% branch coverage?",
  "A defect that requires the execution of a specific path through the code",
  ["A defect in a statement that is never executed",
   "A defect in the false outcome of an IF decision",
   "A defect in the default case of a switch statement"],
  "Ejercitar todas las ramas no garantiza detectar defectos que solo aparecen al recorrer un camino concreto.")
q("4.3.2", "In branch testing, how is coverage measured?",
  "Number of branches exercised by the test cases divided by the total number of branches, as a percentage",
  ["Number of decisions divided by the number of statements",
   "Number of paths divided by the number of branches",
   "Number of failed tests divided by the number of branches"],
  "Cobertura de ramas = ramas ejercitadas / total de ramas, en porcentaje.")
q("4.3.2", "For the code below, which set of tests achieves 100% branch coverage with the minimum number of tests?",
  "x = 5 and x = -5",
  ["x = 5 only", "x = 0 only", "x = 5, x = 6 and x = 7"],
  "Hacen falta las dos salidas de la decisión: x > 0 (p. ej., 5) y x ≤ 0 (p. ej., -5). Un solo valor cubre solo una rama, y 5, 6 y 7 recorren todos la misma.",
  code="IF x > 0 THEN\n    PRINT \"positive\"\nELSE\n    PRINT \"not positive\"\nENDIF")

# ---------------- FL-4.3.3 (K2) Value of white-box testing (7) ----------------
q("4.3.3", "What is a fundamental strength shared by all white-box test techniques?",
  "The entire software implementation is taken into account, which helps detect defects even when the specification is vague, outdated or incomplete",
  ["They can detect missing requirements (defects of omission)",
   "They can be applied before any design exists",
   "They do not require any knowledge of the code"],
  "La fortaleza de la caja blanca es considerar toda la implementación, útil aunque la especificación sea vaga, obsoleta o incompleta.")
q("4.3.3", "What is a corresponding weakness of white-box testing?",
  "If the software does not implement one or more requirements, white-box testing may not detect the resulting defects of omission",
  ["It cannot be used to measure code coverage",
   "It cannot be applied at component level",
   "It always requires an independent test team"],
  "Si un requisito no se implementó, no hay código que cubrir, así que la caja blanca puede no detectar ese defecto de omisión.")
q("4.3.3", "How can white-box test techniques be used in static testing?",
  "For example, during dry runs of code, or reviewing code not yet ready for execution and pseudocode",
  ["They cannot be used in static testing",
   "Only for performance analysis",
   "Only during acceptance testing"],
  "Las técnicas de caja blanca sirven en prueba estática: dry runs de código, revisión de código aún no ejecutable, pseudocódigo y lógica modelable con un grafo de flujo.")
q("4.3.3", "Why is performing only black-box testing considered insufficient for measuring code coverage?",
  "Black-box testing does not provide a measure of actual code coverage",
  ["Black-box testing cannot find any defects",
   "Black-box testing always achieves 100% code coverage",
   "Black-box testing is only allowed at acceptance level"],
  "Solo con caja negra no se mide la cobertura real del código; la caja blanca da una medida objetiva y permite generar pruebas adicionales.")
q("4.3.3", "How do white-box coverage measures help increase confidence in the code?",
  "They provide an objective measurement and the information needed to generate additional tests to increase coverage",
  ["They replace the need for black-box testing",
   "They prove that the code has no defects",
   "They reduce the number of requirements"],
  "Las métricas de cobertura de caja blanca dan una medida objetiva y la información para crear tests adicionales, lo que aumenta la confianza en el código.")
q("4.3.3", "Which of the following can be modelled with a control flow graph and is therefore suitable for white-box techniques in reviews?",
  "Pseudocode and other high-level or top-down logic",
  ["User interface mock-ups",
   "Project budgets",
   "Organization charts"],
  "El syllabus indica que la caja blanca encaja en revisiones de pseudocódigo y otra lógica de alto nivel modelable con un grafo de flujo de control.")
q("4.3.3", "Which coverage-related white-box techniques are mentioned in the syllabus as being outside its scope?",
  "More rigorous techniques used in safety-critical environments and coverage not related to code, such as neuron coverage",
  ["Statement testing",
   "Branch testing",
   "Equivalence partitioning"],
  "El syllabus solo trata prueba de sentencias y de ramas; menciona como fuera de alcance técnicas más rigurosas (entornos críticos), las de niveles superiores (API) y coberturas no basadas en código (cobertura de neuronas).")

# ---------------- FL-4.4.1 (K2) Error guessing (7) ----------------
q("4.4.1", "Which test technique uses the tester's knowledge of past failures and typical developer mistakes to anticipate errors, defects and failures?",
  "Error guessing",
  ["Exploratory testing",
   "Checklist-based testing",
   "Equivalence partitioning"],
  "El error guessing anticipa errores, defectos y fallos basándose en el conocimiento del tester: cómo funcionó la aplicación, errores típicos de los desarrolladores y fallos en aplicaciones similares.")
q("4.4.1", "What are fault attacks?",
  "A methodical way to implement error guessing, using a list of possible errors, defects and failures to design tests that expose them",
  ["Security penetration tests performed by external hackers",
   "A type of static analysis",
   "Tests designed from decision tables"],
  "Los fault attacks son una forma de implementar el error guessing: se crea o adquiere una lista de posibles errores, defectos y fallos y se diseñan tests para provocarlos o exponerlos.")
q("4.4.1", "Which of the following is a source of knowledge for error guessing mentioned in the syllabus?",
  "The types of failures that have occurred in other, similar applications",
  ["The statement coverage achieved",
   "The number of user stories in the backlog",
   "The test completion report template"],
  "Fuentes: cómo funcionó la aplicación en el pasado, los errores típicos de los desarrolladores y los fallos en aplicaciones similares.")
q("4.4.1", "A tester tests an input field with an empty value, a very long string and special characters, because such inputs often caused failures in the past. Which technique is this?",
  "Error guessing",
  ["Boundary value analysis",
   "Decision table testing",
   "Statement testing"],
  "Elegir entradas porque históricamente causan fallos es error guessing (relacionado con errores de entrada).")
q("4.4.1", "Error guessing considers errors related to which areas, according to the syllabus?",
  "Input, output, logic, computation, interfaces and data",
  ["Only the user interface",
   "Only the database",
   "Only performance"],
  "El syllabus enumera: entrada, salida, lógica, cálculo, interfaces y datos.")
q("4.4.1", "How can the lists used in fault attacks be built?",
  "From experience, defect and failure data, or common knowledge about why software fails",
  ["Only from the requirements specification",
   "Only from the code coverage report",
   "Only from the test plan"],
  "Las listas pueden basarse en la experiencia, en datos de defectos y fallos o en el conocimiento común de por qué falla el software.")
q("4.4.1", "\"Wrong operator\" and \"missing cases\" are examples of errors related to which category used in error guessing?",
  "Logic",
  ["Interfaces",
   "Output",
   "Data"],
  "El syllabus da \"missing cases, wrong operator\" como ejemplos de errores de lógica.")

# ---------------- FL-4.4.2 (K2) Exploratory testing (7) ----------------
q("4.4.2", "In which situation is exploratory testing most useful?",
  "When specifications are few or inadequate, or there is significant time pressure on testing",
  ["When exact, repeatable regression scripts are required",
   "When 100% statement coverage must be demonstrated",
   "When the tester has no domain knowledge"],
  "La prueba exploratoria es útil con especificaciones escasas o pobres, con mucha presión de tiempo y para complementar técnicas más formales. Es más eficaz con testers experimentados.")
q("4.4.2", "What characterizes exploratory testing?",
  "Tests are simultaneously designed, executed and evaluated while the tester learns about the test object",
  ["Tests are fully scripted before execution",
   "Tests are derived only from the source code",
   "Tests are executed only by automation tools"],
  "En la prueba exploratoria se diseñan, ejecutan y evalúan pruebas a la vez mientras se aprende sobre el objeto.")
q("4.4.2", "In session-based exploratory testing, what guides the tester during the time-boxed session?",
  "A test charter containing test objectives",
  ["A detailed test procedure",
   "A decision table",
   "The test completion report"],
  "En el enfoque basado en sesiones se trabaja en un timebox guiado por un test charter con objetivos; después suele haber un debriefing.")
q("4.4.2", "What usually follows an exploratory test session in session-based testing?",
  "A debriefing involving a discussion between the tester and stakeholders interested in the results",
  ["A formal inspection of the code",
   "An automated regression run",
   "A new release planning meeting"],
  "Tras la sesión suele haber un debriefing con los stakeholders interesados en los resultados.")
q("4.4.2", "Which statement about exploratory testing is correct?",
  "It can incorporate the use of other test techniques, such as equivalence partitioning",
  ["It cannot be combined with other techniques",
   "It requires complete specifications",
   "It does not involve any coverage items"],
  "La prueba exploratoria puede incorporar otras técnicas, como la partición de equivalencia. Los elementos de cobertura se identifican y ejercitan durante la sesión.")
q("4.4.2", "What can testers use to document the steps followed and the discoveries made during exploratory testing?",
  "Test session sheets",
  ["Decision tables",
   "Risk registers",
   "Control flow graphs"],
  "El tester puede usar hojas de sesión (test session sheets) para documentar los pasos y los hallazgos.")
q("4.4.2", "Exploratory testing will be more effective if the tester:",
  "Is experienced, has domain knowledge and has a high degree of essential skills like curiosity and creativeness",
  ["Has never seen the application before and has no domain knowledge",
   "Follows a fixed script without deviation",
   "Works without any objectives"],
  "El syllabus indica que la prueba exploratoria es más eficaz con testers experimentados, con conocimiento del dominio y con habilidades analíticas, curiosidad y creatividad.")

# ---------------- FL-4.4.3 (K2) Checklist-based testing (7) ----------------
q("4.4.3", "Which items should NOT be included in a checklist used for checklist-based testing?",
  "Items that can be checked automatically, items better suited as entry or exit criteria, or items that are too general",
  ["Items phrased as questions",
   "Items about quality characteristics",
   "Items that can be checked separately and directly"],
  "El syllabus dice que las listas de comprobación no deben incluir elementos comprobables automáticamente, ni otros más adecuados como criterios de entrada o salida, ni demasiado generales.")
q("4.4.3", "Why should checklists be regularly updated based on defect analysis?",
  "Some entries become less effective as developers learn to avoid those errors, and new high-severity defects may need new entries",
  ["Because checklists must always grow in length",
   "Because checklists are only valid for one test run",
   "Because standards require monthly updates"],
  "Algunas entradas pierden eficacia porque los desarrolladores aprenden a evitar esos errores, y hay que añadir otras por nuevos defectos graves, cuidando que la lista no se haga demasiado larga.")
q("4.4.3", "In the absence of detailed test cases, what can checklist-based testing provide?",
  "Guidelines and some degree of consistency for the testing",
  ["Full repeatability of every test",
   "100% code coverage",
   "Proof that the software is correct"],
  "Sin casos detallados, las listas de comprobación dan pautas y cierta consistencia. Si son de alto nivel habrá variabilidad: más cobertura potencial, pero menos repetibilidad.")
q("4.4.3", "What is the effect of using high-level checklists?",
  "Some variability in the actual testing is likely, resulting in potentially greater coverage but less repeatability",
  ["Testing becomes fully repeatable",
   "Coverage always decreases",
   "No tester judgement is needed"],
  "Con listas de alto nivel, cada tester prueba de forma algo distinta: puede aumentar la cobertura, pero se reduce la repetibilidad.")
q("4.4.3", "How are checklist items often phrased?",
  "In the form of a question that can be checked separately and directly",
  ["As detailed test procedures with expected results",
   "As Given/When/Then scenarios",
   "As lines of code"],
  "Los elementos de una lista suelen formularse como preguntas, cada una comprobable por separado y directamente.")
q("4.4.3", "Which of the following is an example of a checklist supporting non-functional testing mentioned in the syllabus?",
  "10 heuristics for usability testing",
  ["A decision table for discounts",
   "A state transition diagram for a login",
   "A risk register"],
  "El syllabus cita las 10 heurísticas de usabilidad (Nielsen) como ejemplo de lista de comprobación para prueba no funcional.")
q("4.4.3", "On which sources can checklists be built?",
  "Experience, knowledge about what is important for the user, or an understanding of why and how software fails",
  ["Only the source code",
   "Only the test execution schedule",
   "Only automated test results"],
  "Las listas pueden basarse en la experiencia, en lo que es importante para el usuario o en entender por qué y cómo falla el software.")

# ---------------- FL-4.5.1 (K2) Collaborative user story writing ----------------
q("4.5.1", "What are the \"3 C's\" of a user story?",
  "Card, Conversation, Confirmation",
  ["Code, Coverage, Criteria",
   "Context, Condition, Case",
   "Collaboration, Communication, Commitment"],
  "Card: el soporte que describe la historia. Conversation: cómo se usará el software. Confirmation: los criterios de aceptación.")
q("4.5.1", "What does the INVEST acronym describe?",
  "Characteristics of good user stories: Independent, Negotiable, Valuable, Estimable, Small and Testable",
  ["Steps of the review process",
   "Test levels in Agile projects",
   "Risk response options"],
  "Las buenas historias de usuario cumplen INVEST: independientes, negociables, valiosas, estimables, pequeñas y comprobables.")
q("4.5.1", "Which three perspectives does collaborative user story writing take into account?",
  "Business, development and testing",
  ["Marketing, sales and finance",
   "Management, legal and operations",
   "Users, auditors and regulators"],
  "La colaboración permite una visión compartida de lo que hay que entregar desde tres perspectivas: negocio, desarrollo y testing.")
q("4.5.1", "If a stakeholder does not know how to test a user story, what may this indicate?",
  "The story may not be clear enough, may not reflect something valuable to them, or they may just need help in testing",
  ["The story must be deleted",
   "The story is ready for implementation",
   "The story should be tested only by developers"],
  "El syllabus indica que puede significar que la historia no está clara, que no refleja algo valioso o que el stakeholder necesita ayuda para probar.")
q("4.5.1", "Which is the most common format for a user story?",
  "As a [role], I want [goal to be accomplished], so that I can [resulting business value for the role]",
  ["Given [precondition], When [action], Then [result]",
   "If [condition] then [action] else [action]",
   "Test ID, steps, expected result"],
  "Formato habitual: \"As a [rol], I want [objetivo], so that I can [valor de negocio]\", seguido de los criterios de aceptación.")
q("4.5.1", "Which techniques can be used for the collaborative authorship of user stories?",
  "Brainstorming and mind mapping",
  ["Static analysis and code reviews",
   "Boundary value analysis and decision tables",
   "Load testing and stress testing"],
  "El syllabus menciona la lluvia de ideas y los mapas mentales.")

# ---------------- FL-4.5.2 (K2) Acceptance criteria ----------------
q("4.5.2", "\"Given the user is logged in, When she adds an item to the cart, Then the cart shows 1 item.\" This acceptance criterion is written in which format?",
  "Scenario-oriented, as used in BDD",
  ["Rule-oriented",
   "A test charter",
   "A test procedure specification"],
  "Given/When/Then es el formato orientado a escenarios (BDD). El orientado a reglas usa listas de verificación o tablas de entrada-salida.")
q("4.5.2", "A list of bullet points such as \"Password must have at least 8 characters\" and \"Password must contain a digit\" is an example of:",
  "Rule-oriented acceptance criteria",
  ["Scenario-oriented acceptance criteria",
   "A user story card",
   "A test log"],
  "Una lista de verificación con viñetas (o una tabla de entrada-salida) es el formato orientado a reglas.")
q("4.5.2", "Which of the following is a purpose of acceptance criteria?",
  "To define the scope of the user story and reach consensus among stakeholders",
  ["To replace the user story",
   "To define the developer's coding standards",
   "To list the defects found in production"],
  "Sirven para definir el alcance, lograr consenso, describir escenarios positivos y negativos, servir de base a la aceptación y permitir planificar y estimar con precisión.")
q("4.5.2", "Acceptance criteria are usually a result of which of the 3 C's?",
  "Conversation",
  ["Card",
   "Commitment",
   "Coverage"],
  "El syllabus indica que los criterios de aceptación suelen resultar de la Conversation; los propios criterios son la Confirmation. \"Commitment\" y \"Coverage\" no forman parte de las 3 C.")
q("4.5.2", "From a testing perspective, acceptance criteria may be viewed as:",
  "The test conditions that should be exercised by the tests",
  ["The test environment requirements",
   "The exit criteria of the whole project",
   "The defect reports of the user story"],
  "Los criterios de aceptación pueden verse como las condiciones de prueba que deben ejercitarse.")
q("4.5.2", "Can a team use a custom format for acceptance criteria instead of scenario-oriented or rule-oriented formats?",
  "Yes, as long as the acceptance criteria are well-defined and unambiguous",
  ["No, only Given/When/Then is allowed",
   "No, only bullet point lists are allowed",
   "Yes, but only if the product owner writes them alone"],
  "El syllabus permite un formato propio siempre que los criterios estén bien definidos y no sean ambiguos.")
