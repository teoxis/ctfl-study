from qlib import q

# ---------------- FL-2.1.1 (K2) Impact of the SDLC on testing ----------------
q("2.1.1", "In a sequential development model, what do testers typically do in the initial phases?",
  "Participate in requirement reviews, test analysis and test design",
  ["Execute dynamic tests on the complete system",
   "Run automated regression tests in the CI pipeline",
   "Perform user acceptance testing"],
  "En modelos secuenciales el código ejecutable llega tarde, así que al principio los testers participan en revisiones de requisitos, análisis y diseño; la prueba dinámica no puede hacerse pronto.")
q("2.1.1", "Which of the following is impacted by the choice of SDLC, according to the syllabus?",
  "The extent of test automation and the level of detail of test documentation",
  ["The seven testing principles",
   "The definition of a defect",
   "The ISTQB glossary terms"],
  "La elección del ciclo de vida afecta al alcance y momento de las actividades, al detalle de la documentación, a técnicas y enfoque, al grado de automatización y al papel del tester.")
q("2.1.1", "Why are lightweight documentation and extensive test automation favored in Agile projects?",
  "Because Agile assumes change may occur throughout the project, so regression testing must be easy",
  ["Because Agile projects do not need regression testing",
   "Because Agile forbids written test cases",
   "Because automation removes the need for testers"],
  "El desarrollo ágil asume cambios continuos; por eso se prefiere documentación ligera y mucha automatización que facilite la regresión.")
q("2.1.1", "In iterative and incremental models where each iteration delivers a working increment, which statement is correct?",
  "Both static and dynamic testing may be performed at all test levels in each iteration",
  ["Dynamic testing can only start after the last iteration",
   "Only acceptance testing is performed in each iteration",
   "Regression testing is unnecessary because increments are small"],
  "Si cada iteración entrega un incremento funcional, en cada una pueden hacerse pruebas estáticas y dinámicas en todos los niveles. La entrega frecuente exige feedback rápido y mucha regresión.")
q("2.1.1", "In Agile development, which kind of test techniques tend to be used for most of the manual testing?",
  "Experience-based test techniques that do not require extensive prior test analysis and design",
  ["White-box techniques based on detailed design documents",
   "Formal techniques requiring complete specifications",
   "Only boundary value analysis"],
  "El syllabus indica que en ágil la mayor parte de la prueba manual se hace con técnicas basadas en la experiencia, que no exigen un análisis y diseño previos extensos.")
q("2.1.1", "What does frequent delivery of increments in iterative development require from testing?",
  "Fast feedback and extensive regression testing",
  ["Fewer test levels",
   "Longer test cycles at the end of the project",
   "No static testing"],
  "Entregar incrementos con frecuencia exige feedback rápido y regresión extensa.")

# ---------------- FL-2.1.2 (K1) Good practices for all SDLCs (10) ----------------
q("2.1.2", "Which of the following is a good testing practice that applies regardless of the SDLC?",
  "For every software development activity there is a corresponding test activity",
  ["Testing starts only after coding is complete",
   "Every test level has the same test objectives",
   "Testers should not review draft work products"],
  "Buenas prácticas para cualquier ciclo de vida: a cada actividad de desarrollo le corresponde una de prueba, cada nivel tiene objetivos específicos, el análisis y diseño empiezan en la fase correspondiente, y los testers revisan borradores en cuanto existen.")
q("2.1.2", "Why should different test levels have specific and different test objectives?",
  "So that testing is appropriately comprehensive while avoiding redundancy",
  ["So that each level can be skipped if the previous one passed",
   "So that each level is performed by the same people",
   "So that no test level needs exit criteria"],
  "Objetivos distintos por nivel permiten que la prueba sea completa sin solaparse innecesariamente.")
q("2.1.2", "When should test analysis and design for a given test level begin?",
  "During the corresponding development phase of the SDLC",
  ["After the code for that level is complete",
   "At the end of the project",
   "Only after the previous test level has finished execution"],
  "El análisis y diseño de un nivel empieza en la fase de desarrollo correspondiente, en línea con el principio de prueba temprana.")
q("2.1.2", "When should testers be involved in reviewing work products?",
  "As soon as drafts of these work products are available",
  ["Only after the work products have been formally approved",
   "Only during test execution",
   "Only when defects have been reported in production"],
  "Revisar borradores en cuanto existen favorece la detección temprana de defectos y el shift left.")
q("2.1.2", "Which good practice ensures that all development activities are subject to quality control?",
  "Having a corresponding test activity for every development activity",
  ["Automating all tests",
   "Performing only exploratory testing",
   "Having a single test level"],
  "Que cada actividad de desarrollo tenga su actividad de prueba garantiza que todo el desarrollo esté sujeto a control de calidad.")
q("2.1.2", "Starting test analysis and design during the corresponding development phase helps testing adhere to which principle?",
  "Early testing saves time and money",
  ["Tests wear out",
   "Defects cluster together",
   "Absence-of-defects fallacy"],
  "El syllabus vincula explícitamente esta buena práctica con el principio de prueba temprana.")
q("2.1.2", "Which statement is NOT one of the good testing practices that apply to all SDLCs?",
  "Dynamic testing must be completed before any reviews take place",
  ["For every development activity there is a corresponding test activity",
   "Different test levels have specific and different test objectives",
   "Testers review work products as soon as drafts are available"],
  "Exigir pruebas dinámicas antes de las revisiones va contra el shift left. Las otras tres opciones son buenas prácticas del syllabus.")
q("2.1.2", "Testers reviewing drafts of work products as soon as they are available supports which approach?",
  "Shift left",
  ["Big-bang integration",
   "Exhaustive testing",
   "Independent acceptance testing"],
  "El syllabus dice que esta práctica permite detectar defectos antes y apoya el shift left.")
q("2.1.2", "A V-model project and a Scrum project both want to follow good testing practices. Which practice is valid for both?",
  "Test analysis and design for each test level begins during the corresponding development phase",
  ["All testing is postponed until the system is complete",
   "Only one test level is used",
   "Test cases are written after the release"],
  "Las buenas prácticas de 2.1.2 son independientes del modelo de ciclo de vida elegido.")
q("2.1.2", "Which good practice helps avoid redundant testing across test levels?",
  "Giving each test level specific and different test objectives",
  ["Running every test case at every level",
   "Assigning the same tester to all levels",
   "Skipping integration testing"],
  "Que cada nivel tenga objetivos propios permite ser completo evitando redundancias.")

# ---------------- FL-2.1.3 (K1) Test-first approaches (10) ----------------
q("2.1.3", "Which statement about test-driven development (TDD) is correct?",
  "Tests are written first, then code is written to satisfy the tests, and then the tests and code are refactored",
  ["Tests are written in Given/When/Then natural language for stakeholders",
   "Tests are derived collaboratively from acceptance criteria during system design",
   "Tests are written after the code is complete to check the implemented design"],
  "TDD dirige la codificación mediante casos de prueba: test → código → refactorización. Given/When/Then es BDD; derivar tests de criterios de aceptación es ATDD.")
q("2.1.3", "Which test-first approach expresses the desired behavior with test cases written in simple natural language, usually in the Given/When/Then format?",
  "Behavior-driven development (BDD)",
  ["Test-driven development (TDD)",
   "Acceptance test-driven development (ATDD)",
   "Feature-driven development (FDD)"],
  "BDD expresa el comportamiento en lenguaje natural sencillo, normalmente Given/When/Then, y esos casos se traducen después en pruebas ejecutables.")
q("2.1.3", "Which test-first approach derives tests from acceptance criteria as part of the system design process?",
  "Acceptance test-driven development (ATDD)",
  ["Test-driven development (TDD)",
   "Behavior-driven development (BDD)",
   "Domain-driven design (DDD)"],
  "ATDD deriva las pruebas de los criterios de aceptación durante el diseño del sistema, y se escriben antes de desarrollar esa parte de la aplicación.")
q("2.1.3", "What do TDD, ATDD and BDD have in common?",
  "Tests are defined before the code is written, following the principle of early testing and shift left",
  ["They all require a sequential SDLC",
   "They all use only manual tests",
   "They all postpone testing to the end of the iteration"],
  "Los tres definen las pruebas antes de escribir el código, aplican la prueba temprana, siguen el shift left y apoyan un modelo iterativo.")
q("2.1.3", "In TDD, what directs the coding instead of extensive software design?",
  "Test cases",
  ["User manuals",
   "Defect reports",
   "Architecture diagrams"],
  "Según el syllabus, TDD dirige la codificación a través de casos de prueba, en lugar de un diseño de software extenso.")
q("2.1.3", "In BDD, what should happen to the test cases written in natural language?",
  "They should be automatically translated into executable tests",
  ["They should be archived without execution",
   "They should be executed only manually",
   "They should replace the source code"],
  "En BDD, los casos en lenguaje natural deben traducirse automáticamente en pruebas ejecutables.")
q("2.1.3", "Which statement applies to tests created with TDD, ATDD and BDD?",
  "They may persist as automated tests to ensure code quality in future adaptations and refactoring",
  ["They must be deleted after the feature is released",
   "They can only be run once",
   "They are only useful for performance testing"],
  "Las pruebas de estos enfoques pueden mantenerse como pruebas automatizadas para asegurar la calidad del código en futuras adaptaciones o refactorizaciones.")
q("2.1.3", "Which type of development model do TDD, ATDD and BDD support?",
  "An iterative development model",
  ["Only the waterfall model",
   "Only the V-model",
   "Only big-bang development"],
  "El syllabus indica que estos enfoques apoyan un modelo de desarrollo iterativo.")
q("2.1.3", "A team writes component tests in a unit test framework before writing the code, then makes them pass and refactors. Which approach are they using?",
  "Test-driven development (TDD)",
  ["Behavior-driven development (BDD)",
   "Acceptance test-driven development (ATDD)",
   "Exploratory testing"],
  "Escribir tests antes del código, hacerlos pasar y refactorizar es el ciclo de TDD.")
q("2.1.3", "In ATDD, when are the tests written?",
  "Before the part of the application is developed to satisfy the tests",
  ["After the user story is released to production",
   "During the sprint retrospective",
   "Only after a defect is found"],
  "En ATDD las pruebas se escriben antes de desarrollar la parte de la aplicación que debe satisfacerlas.")

# ---------------- FL-2.1.4 (K2) DevOps and testing ----------------
q("2.1.4", "Which of the following is a benefit of DevOps for testing?",
  "Fast feedback on code quality and on whether changes adversely affect existing code",
  ["Manual testing is no longer needed",
   "Test environments are no longer required",
   "Non-functional testing becomes unnecessary"],
  "Beneficios: feedback rápido, CI que promueve el shift left, entornos estables por automatización, más visibilidad de lo no funcional, menos prueba manual repetitiva y menor riesgo de regresión.")
q("2.1.4", "Which of the following is a risk or challenge of DevOps mentioned in the syllabus?",
  "Test automation requires additional resources and may be difficult to establish and maintain",
  ["Developers stop writing component tests",
   "Feedback on code quality becomes slower",
   "Non-functional characteristics become less visible"],
  "Riesgos: hay que definir y establecer el pipeline, introducir y mantener herramientas CI/CD, y la automatización exige recursos y puede ser difícil de mantener.")
q("2.1.4", "How does continuous integration (CI) promote shift left in testing?",
  "By encouraging developers to submit high quality code accompanied by component tests and static analysis",
  ["By postponing testing until the release",
   "By replacing all manual testing with exploratory testing",
   "By removing the need for code reviews"],
  "La CI anima a los desarrolladores a enviar código de calidad acompañado de pruebas de componente y análisis estático, lo que adelanta la prueba.")
q("2.1.4", "Which statement about manual testing in DevOps is correct?",
  "Manual testing, especially from the user's perspective, will still be needed",
  ["Manual testing is eliminated completely",
   "Manual testing is only done by developers",
   "Manual testing is only done in production"],
  "Aunque DevOps implica mucha prueba automatizada, sigue haciendo falta prueba manual, sobre todo desde la perspectiva del usuario.")
q("2.1.4", "Why is the risk of regression minimized in a DevOps environment?",
  "Because of the scale and range of automated regression tests",
  ["Because code changes are no longer allowed",
   "Because testers review every commit manually",
   "Because DevOps does not use test environments"],
  "El syllabus atribuye la reducción del riesgo de regresión a la escala y amplitud de las pruebas de regresión automatizadas.")
q("2.1.4", "What does DevOps require within an organization?",
  "A cultural shift to bridge the gaps between development (including testing) and operations",
  ["Separating testing from development",
   "Eliminating the operations team",
   "Replacing CI with manual deployment"],
  "DevOps exige un cambio cultural que una desarrollo (incluidas las pruebas) y operaciones, valorando por igual sus funciones.")

# ---------------- FL-2.1.5 (K2) Shift left ----------------
q("2.1.5", "Which of the following is an example of the shift-left approach?",
  "Reviewing the specification from the perspective of testers before coding starts",
  ["Running performance tests only in production",
   "Postponing static analysis until system testing",
   "Writing test cases after the product has been released"],
  "Prácticas de shift left: revisar especificaciones desde la perspectiva del tester, escribir tests antes del código, usar CI/CD, análisis estático antes de la prueba dinámica, y pruebas no funcionales desde el nivel de componente.")
q("2.1.5", "Which statement about shift left is correct?",
  "Testing should be done earlier, but testing later in the SDLC should not be neglected",
  ["All testing must be completed before coding starts",
   "Shift left means that system testing is no longer necessary",
   "Shift left reduces the costs early in the process"],
  "Shift left propone probar antes, pero no implica descuidar las pruebas posteriores. Puede suponer más formación, esfuerzo o coste al principio a cambio de ahorrar después.")
q("2.1.5", "Performing non-functional testing starting at the component test level is:",
  "A form of shift left",
  ["A violation of good testing practices",
   "Only possible in sequential models",
   "A form of maintenance testing"],
  "Las pruebas no funcionales suelen hacerse tarde, con el sistema completo; empezarlas en el nivel de componente, cuando es posible, es una forma de shift left.")
q("2.1.5", "What is an important precondition for shift left to succeed?",
  "Stakeholders are convinced and bought into the concept",
  ["The project uses a waterfall model",
   "Testers are fully independent from developers",
   "No test automation is used"],
  "El syllabus señala que para el shift left es importante que los stakeholders estén convencidos y comprometidos con el concepto.")
q("2.1.5", "What is the expected cost effect of shift left?",
  "It might cause extra training, effort or costs earlier, but is expected to save effort or costs later",
  ["It always reduces costs in every phase",
   "It increases costs later in the process",
   "It has no effect on costs"],
  "Shift left puede requerir inversión temprana (formación, esfuerzo, costes) que se espera recuperar con ahorros posteriores.")
q("2.1.5", "Completing static analysis of source code prior to dynamic testing is an example of:",
  "Shift left",
  ["Regression testing",
   "Confirmation testing",
   "Acceptance testing"],
  "El syllabus lo cita como práctica de shift left, sobre todo si forma parte de un proceso automatizado.")

# ---------------- FL-2.1.6 (K2) Retrospectives ----------------
q("2.1.6", "Which question is typically discussed in a retrospective?",
  "What was not successful and could be improved?",
  ["Which developer caused the most defects?",
   "Which test cases can be deleted to finish faster?",
   "How can the release date be hidden from stakeholders?"],
  "En una retrospectiva se discute qué fue bien y debe mantenerse, qué no fue bien y puede mejorarse, y cómo incorporar las mejoras.")
q("2.1.6", "Where are the results of retrospectives normally recorded?",
  "In the test completion report",
  ["In the defect reports",
   "In the test plan of the previous project",
   "They are never recorded"],
  "El syllabus dice que los resultados deben registrarse y normalmente forman parte del informe de finalización.")
q("2.1.6", "Which of the following is a typical benefit of retrospectives for testing?",
  "Increased test effectiveness and efficiency through process improvement suggestions",
  ["Elimination of the need for regression testing",
   "Guarantee of zero defects in the next iteration",
   "Reduction of the number of stakeholders"],
  "Beneficios: más eficacia y eficiencia, mejor testware, cohesión y aprendizaje del equipo, mejor base de prueba y mejor cooperación entre desarrollo y testing.")
q("2.1.6", "Who participates in retrospectives?",
  "Not only testers but also, e.g., developers, architects, product owner and business analysts",
  ["Only testers",
   "Only the test manager and the project sponsor",
   "Only external auditors"],
  "Participan testers y otros perfiles: desarrolladores, arquitectos, product owner, analistas de negocio…")
q("2.1.6", "What is critical for retrospectives to support continuous improvement?",
  "Recommended improvements are followed up",
  ["Retrospectives are held only once per project",
   "Only successes are discussed",
   "Results are kept confidential within the test team"],
  "Las retrospectivas son clave para la mejora continua, y es importante hacer seguimiento de las mejoras recomendadas.")
q("2.1.6", "How can retrospectives improve the quality of the test basis?",
  "Deficiencies in the extent and quality of the requirements can be addressed and solved",
  ["By removing all non-functional requirements",
   "By letting testers rewrite requirements without stakeholders",
   "By freezing requirements for the rest of the project"],
  "Uno de los beneficios citados es mejorar la base de prueba, abordando deficiencias en el alcance y la calidad de los requisitos.")

# ---------------- FL-2.2.1 (K2) Test levels ----------------
q("2.2.1", "Which test level focuses on the interfaces and interactions between components?",
  "Component integration testing",
  ["Component testing",
   "System testing",
   "Acceptance testing"],
  "La integración de componentes prueba interfaces e interacciones entre componentes y depende mucho de la estrategia de integración (bottom-up, top-down, big-bang).")
q("2.2.1", "Which test level focuses on validation and on demonstrating readiness for deployment?",
  "Acceptance testing",
  ["System integration testing",
   "Component testing",
   "Component integration testing"],
  "La aceptación se centra en validar y demostrar que el sistema está listo para desplegarse, idealmente con los usuarios previstos.")
q("2.2.1", "Testing the interfaces between the system under test and an external payment service belongs to which test level?",
  "System integration testing",
  ["Component integration testing",
   "Component testing",
   "Acceptance testing"],
  "La integración de sistemas prueba interfaces con otros sistemas y servicios externos, preferiblemente en entornos similares al operativo.")
q("2.2.1", "Which statement about component testing is correct?",
  "It focuses on testing components in isolation and often requires test harnesses or unit test frameworks",
  ["It is normally performed by business representatives",
   "It requires a production-like environment",
   "It focuses on end-to-end business processes"],
  "La prueba de componente (unit testing) prueba componentes aislados, suele necesitar harnesses o frameworks y la hacen normalmente los desarrolladores en su entorno.")
q("2.2.1", "Which test level focuses on the overall behavior and capabilities of an entire system, often including end-to-end functional tasks and non-functional quality characteristics?",
  "System testing",
  ["Component integration testing",
   "Component testing",
   "System integration testing"],
  "La prueba de sistema evalúa el comportamiento global del sistema completo, incluidas tareas extremo a extremo y características no funcionales, y puede hacerla un equipo independiente.")
q("2.2.1", "Which attribute is used in the syllabus to distinguish test levels and avoid overlapping test activities?",
  "Test objectives",
  ["The number of testers",
   "The tool vendor",
   "The colour of the test reports"],
  "Atributos para distinguir niveles: objeto de prueba, objetivos, base de prueba, defectos y fallos, y enfoque y responsabilidades.")
q("2.2.1", "Which of the following is listed in the syllabus as a main form of acceptance testing?",
  "Operational acceptance testing",
  ["Component integration testing",
   "Static analysis",
   "Mutation testing"],
  "Formas de aceptación: UAT, operacional, contractual y regulatoria, alfa y beta.")

# ---------------- FL-2.2.2 (K2) Test types ----------------
q("2.2.2", "Measuring the response time of a search page with 500 concurrent users is an example of which test type?",
  "Non-functional testing",
  ["Functional testing",
   "White-box testing",
   "Confirmation testing"],
  "La eficiencia de desempeño es una característica no funcional: mide \"cómo de bien\" se comporta el sistema.")
q("2.2.2", "What is the main objective of functional testing?",
  "Checking functional completeness, functional correctness and functional appropriateness",
  ["Checking the internal structure of the code",
   "Checking performance efficiency and security",
   "Checking that a fix has not broken anything else"],
  "La prueba funcional evalúa \"qué\" debe hacer el sistema: completitud, corrección y adecuación funcionales.")
q("2.2.2", "Which test type derives tests from the system's implementation or internal structure, such as code, architecture or data flows?",
  "White-box testing",
  ["Black-box testing",
   "Non-functional testing",
   "Acceptance testing"],
  "La prueba de caja blanca se basa en la estructura; su objetivo principal es cubrir esa estructura hasta un nivel aceptable.")
q("2.2.2", "Which statement about test types and test levels is correct?",
  "All four test types can be applied at all test levels, although the focus differs at each level",
  ["Functional testing can only be performed at system level",
   "White-box testing can only be performed at component level",
   "Non-functional testing can only be performed at acceptance level"],
  "Los cuatro tipos (funcional, no funcional, caja negra y caja blanca) pueden aplicarse en todos los niveles, con distinto foco.")
q("2.2.2", "Which of the following is a non-functional quality characteristic in the ISO/IEC 25010 classification listed in the syllabus?",
  "Portability (also known as flexibility)",
  ["Functional correctness",
   "Statement coverage",
   "Traceability"],
  "Características no funcionales del syllabus: eficiencia de desempeño, compatibilidad, usabilidad (capacidad de interacción), fiabilidad, seguridad, mantenibilidad, portabilidad (flexibilidad) y safety.")
q("2.2.2", "Why can late discovery of non-functional defects be dangerous?",
  "It can pose a serious threat to the success of a project",
  ["Non-functional defects cannot be fixed at all",
   "Non-functional defects always cause data loss",
   "Non-functional testing is not allowed late in the SDLC"],
  "El syllabus advierte que descubrir tarde defectos no funcionales puede poner en serio peligro el proyecto; por eso a veces conviene empezar pronto.")
q("2.2.2", "Which test type is specification-based and checks the system's behavior against its specifications?",
  "Black-box testing",
  ["White-box testing",
   "Structural testing",
   "Static analysis"],
  "La prueba de caja negra se basa en la especificación y deriva pruebas de documentación no relacionada con la estructura interna.")

# ---------------- FL-2.2.3 (K2) Confirmation vs regression ----------------
q("2.2.3", "After a defect is fixed, a tester re-runs the test that failed and it now passes. Then she runs other tests to check that nothing else was broken. Which statement is correct?",
  "The first run is confirmation testing; the second is regression testing",
  ["The first run is regression testing; the second is confirmation testing",
   "Both runs are confirmation testing",
   "Both runs are regression testing"],
  "La confirmación comprueba que el defecto original se ha corregido; la regresión, que el cambio no ha tenido consecuencias adversas en otras partes.")
q("2.2.3", "When time or money is short, confirmation testing might be restricted to:",
  "Exercising the steps that should reproduce the failure and checking that it no longer occurs",
  ["Running the complete regression suite",
   "Skipping testing of the fix entirely",
   "Reviewing the code change only"],
  "El syllabus permite, con poco tiempo o dinero, limitar la confirmación a reproducir los pasos del fallo y comprobar que ya no ocurre.")
q("2.2.3", "What is advisable before regression testing, to recognize its extent?",
  "Performing an impact analysis",
  ["Writing a new test plan",
   "Running exploratory testing",
   "Repeating confirmation testing"],
  "Conviene hacer primero un análisis de impacto, que muestra qué partes del software podrían verse afectadas.")
q("2.2.3", "Why is regression testing a strong candidate for automation?",
  "Regression test suites are run many times and generally grow with each iteration or release",
  ["Regression tests never need maintenance",
   "Regression tests cannot be executed manually",
   "Regression testing is only done once per project"],
  "Las suites de regresión se ejecutan muchas veces y crecen con cada iteración, así que son ideales para automatizar, empezando pronto.")
q("2.2.3", "Which of the following can be affected by the adverse consequences that regression testing tries to detect?",
  "The same component, other components in the same system, or even other connected systems",
  ["Only the line of code that was changed",
   "Only the user documentation",
   "Only the test environment"],
  "Las consecuencias adversas pueden afectar al mismo componente, a otros del sistema o incluso a sistemas conectados, y también al entorno.")
q("2.2.3", "At which test levels are confirmation and regression testing needed?",
  "On all test levels where defects are fixed or changes are made",
  ["Only at the system test level",
   "Only at the acceptance test level",
   "Only in maintenance testing"],
  "El syllabus indica que se necesitan en todos los niveles donde se corrijan defectos o se hagan cambios.")

# ---------------- FL-2.3.1 (K2) Maintenance testing ----------------
q("2.3.1", "Which of the following is a trigger for maintenance testing?",
  "Migrating the system from one platform to another",
  ["Writing the first user stories of a new product",
   "Integrating a new system for the first time before its initial release",
   "Designing the architecture of a new product"],
  "Disparadores: modificaciones (mejoras, correcciones, hot fixes), actualizaciones o migraciones del entorno operativo, y retirada del sistema.")
q("2.3.1", "When a system is retired, which testing may be required?",
  "Testing of data archiving, and of restore and retrieval procedures if data must be kept",
  ["Usability testing of the new user interface",
   "Component testing of new features",
   "Performance testing under peak load"],
  "Al retirar un sistema puede hacer falta probar el archivado de datos y los procedimientos de restauración y recuperación durante el periodo de archivo.")
q("2.3.1", "On which factors does the scope of maintenance testing typically depend?",
  "The degree of risk of the change, the size of the existing system and the size of the change",
  ["The number of testers available only",
   "The age of the development team",
   "The programming language of the test tools"],
  "El alcance depende del riesgo del cambio, del tamaño del sistema existente y del tamaño del cambio.")
q("2.3.1", "Data from another application is migrated into the system being maintained. Which testing is typically needed?",
  "Testing of the data conversion",
  ["Only static analysis of the source code",
   "Only alpha testing",
   "No testing, because no code has changed"],
  "Las migraciones pueden requerir pruebas del nuevo entorno, del software cambiado y de la conversión de datos.")
q("2.3.1", "Why may impact analysis be done before a change is made to an operational system?",
  "To help decide whether the change should be made, based on its potential consequences",
  ["To replace regression testing",
   "To calculate the developer's bonus",
   "To avoid testing the change"],
  "El análisis de impacto previo ayuda a decidir si hacer el cambio según sus posibles consecuencias en otras áreas del sistema.")
q("2.3.1", "Testing a change to an operational system includes which of the following?",
  "Evaluating the success of the change and checking for regressions in the unchanged parts",
  ["Only testing the changed code",
   "Only re-running acceptance tests from the first release",
   "Only checking the release notes"],
  "La prueba de mantenimiento evalúa el éxito del cambio y comprueba posibles regresiones en las partes no modificadas, que suelen ser la mayor parte del sistema.")
