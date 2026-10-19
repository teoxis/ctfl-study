from qlib import q

# ---------------- FL-5.1.1 (K2) Test plan ----------------
q("5.1.1", "Which of the following is typically part of a test plan?",
  "The test approach, including test levels, test types, test techniques and entry and exit criteria",
  ["Detailed defect reports with steps to reproduce",
   "The root cause analysis of production failures",
   "Test logs from the previous release"],
  "Contenido típico: contexto, supuestos y restricciones, stakeholders, comunicación, registro de riesgos, enfoque de prueba, presupuesto y calendario.")
q("5.1.1", "Which of the following is a purpose of a test plan?",
  "It serves as a means of communication with team members and other stakeholders",
  ["It replaces the test strategy of the organization",
   "It records the actual results of test execution",
   "It lists all defects found in production"],
  "Un plan documenta medios y calendario, ayuda a cumplir los criterios, sirve para comunicarse y demuestra la adherencia a la política y estrategia de prueba (o explica las desviaciones).")
q("5.1.1", "How does test planning help testers, according to the syllabus?",
  "It guides their thinking and forces them to confront future challenges related to risks, schedules, people, tools, costs and effort",
  ["It removes the need for test monitoring",
   "It guarantees that the plan will never change",
   "It ensures no defects will be found"],
  "Preparar el plan obliga a pensar en los retos futuros (riesgos, calendario, personas, herramientas, costes, esfuerzo).")
q("5.1.1", "In a test plan, where would you typically find hiring and training needs?",
  "In the stakeholders section (roles, responsibilities, relevance to testing, hiring and training needs)",
  ["In the risk register",
   "In the budget and schedule section",
   "In the communication section"],
  "El syllabus sitúa las necesidades de contratación y formación dentro del apartado de stakeholders del plan.")
q("5.1.1", "Which standard provides more details about the test plan and its content?",
  "ISO/IEC/IEEE 29119-3",
  ["ISO/IEC 20246",
   "ISO/IEC 25010",
   "ISO 31000"],
  "La norma ISO/IEC/IEEE 29119-3 trata la documentación de pruebas, incluido el plan.")
q("5.1.1", "A test plan explains why testing will deviate from the organization's test strategy. Which purpose of the test plan does this serve?",
  "Demonstrating that testing will adhere to the test policy and test strategy, or explaining why it will deviate from them",
  ["Recording test results",
   "Defining the product requirements",
   "Calculating defect density"],
  "Uno de los propósitos del plan es demostrar la adherencia a la política y estrategia de prueba o explicar las desviaciones.")

# ---------------- FL-5.1.2 (K1) Tester in iteration and release planning ----------------
q("5.1.2", "How does a tester typically contribute to release planning?",
  "By participating in writing testable user stories and acceptance criteria, and in project and quality risk analyses",
  ["By breaking down user stories into coding tasks only",
   "By approving the release budget",
   "By deciding the release date alone"],
  "En release planning, los testers participan en escribir historias y criterios comprobables, en análisis de riesgos de proyecto y calidad, estiman esfuerzo, determinan el enfoque y planifican las pruebas de la release.")
q("5.1.2", "How does a tester typically contribute to iteration planning?",
  "By participating in the detailed risk analysis of user stories and determining their testability",
  ["By defining the product vision",
   "By deciding the order of all releases for the next year",
   "By writing the marketing plan"],
  "En iteration planning, los testers analizan en detalle los riesgos de las historias, determinan su testabilidad, las dividen en tareas (sobre todo de prueba), estiman y refinan aspectos funcionales y no funcionales.")
q("5.1.2", "Which planning activity looks ahead to the end of a single iteration and is concerned with the iteration backlog?",
  "Iteration planning",
  ["Release planning",
   "Test strategy definition",
   "Portfolio planning"],
  "La iteration planning mira al final de una iteración y trabaja con el backlog de la iteración; la release planning mira a la release y al product backlog.")
q("5.1.2", "Which statement about release planning is correct?",
  "It serves as the basis for the test approach and test plan across all iterations",
  ["It only covers a single iteration",
   "It is performed only by developers",
   "It never involves refining user stories"],
  "La release planning define y redefine el product backlog, puede dividir historias grandes y es la base del enfoque y del plan de prueba de todas las iteraciones.")
q("5.1.2", "During iteration planning, testers break down user stories into:",
  "Tasks, particularly testing tasks",
  ["Epics",
   "Releases",
   "Test policies"],
  "Los testers dividen las historias en tareas (sobre todo de prueba) y estiman el esfuerzo de todas ellas.")
q("5.1.2", "In which kind of SDLC do release planning and iteration planning typically occur?",
  "Iterative SDLCs",
  ["Only the waterfall model",
   "Only the V-model",
   "Only maintenance projects"],
  "El syllabus indica que en ciclos de vida iterativos suelen darse dos tipos de planificación: de release y de iteración.")

# ---------------- FL-5.1.3 (K2) Entry and exit criteria ----------------
q("5.1.3", "Which of the following is a typical EXIT criterion?",
  "The planned level of coverage has been achieved and the number of unresolved defects is acceptable",
  ["Testable requirements are available",
   "The test environment is ready",
   "All smoke tests have passed"],
  "Salida: medidas de exhaustividad (cobertura, defectos sin resolver, densidad, tests fallidos) y criterios sí/no. Requisitos disponibles, entorno listo y smoke tests superados son criterios de entrada.")
q("5.1.3", "Which of the following is a typical ENTRY criterion?",
  "Availability of resources such as people, tools, environments and test data",
  ["Achieved level of coverage",
   "All regression tests are automated",
   "Defect density below the target"],
  "Entrada: disponibilidad de recursos y testware, y nivel de calidad inicial del objeto de prueba (p. ej., smoke tests superados).")
q("5.1.3", "In Agile software development, what are exit criteria often called?",
  "Definition of Done",
  ["Definition of Ready",
   "Acceptance criteria",
   "Test charter"],
  "Los criterios de salida suelen llamarse Definition of Done; los criterios de entrada de una historia, Definition of Ready.")
q("5.1.3", "Under what circumstance can running out of time or budget be a valid exit criterion?",
  "When stakeholders have reviewed and accepted the risk of going live without further testing",
  ["Never; testing must continue until all defects are fixed",
   "Only if the testers decide so",
   "Only in safety-critical projects"],
  "Quedarse sin tiempo o presupuesto puede ser válido si los stakeholders aceptan el riesgo de salir sin más pruebas.")
q("5.1.3", "What is likely to happen if entry criteria are not met?",
  "The activity will likely prove more difficult, time-consuming, costly and riskier",
  ["The activity becomes faster",
   "Exit criteria are automatically met",
   "Nothing; entry criteria are only informative"],
  "El syllabus advierte que, sin cumplir los criterios de entrada, la actividad será probablemente más difícil, larga, cara y arriesgada.")
q("5.1.3", "Which statement about entry and exit criteria is correct?",
  "They should be defined for each test level and will differ based on the test objectives",
  ["They are the same for every test level",
   "Only exit criteria are needed",
   "They are defined only after testing has finished"],
  "Los criterios de entrada y salida deben definirse para cada nivel y difieren según los objetivos.")

# ---------------- FL-5.1.6 (K1) Test pyramid ----------------
q("5.1.6", "What does the test pyramid model suggest?",
  "Many small, fast, isolated tests at the lower layers and fewer, slower, end-to-end tests at the higher layers",
  ["Most automated tests should be end-to-end tests through the UI",
   "All layers should contain the same number of tests",
   "Lower-layer tests are slower and more expensive than higher-layer tests"],
  "Cuanto más alta la capa: menos granularidad, menos aislamiento y más tiempo de ejecución. Abajo hacen falta muchos tests; arriba, pocos.")
q("5.1.6", "Which three layers does the original test pyramid model by Cohn define?",
  "Unit tests, service tests and UI tests",
  ["Component tests, system tests and acceptance tests",
   "Static tests, dynamic tests and manual tests",
   "Smoke tests, regression tests and exploratory tests"],
  "El modelo original (Cohn 2009) define unit, service y UI tests. Otro modelo popular usa unit, integration y end-to-end.")
q("5.1.6", "In the test pyramid, what happens as you move to a higher layer?",
  "Test granularity and isolation decrease, and test execution time increases",
  ["Test granularity increases and execution time decreases",
   "Tests become more isolated and faster",
   "The number of tests needed increases"],
  "Más arriba: menor granularidad, menor aislamiento (más dependencia de otros elementos) y más tiempo de ejecución.")
q("5.1.6", "How does the test pyramid support the team?",
  "In test automation and test effort allocation, by showing that different test objectives are supported by different levels of automation",
  ["By defining the order of test levels in a sequential model",
   "By determining the risk level of each test",
   "By replacing the test plan"],
  "La pirámide apoya la automatización y la asignación de esfuerzo mostrando que distintos objetivos se cubren con distintos niveles de automatización.")
q("5.1.6", "Which statement about the layers of the test pyramid is correct?",
  "The number and naming of the layers may differ between models",
  ["There must always be exactly three layers named unit, integration and UI",
   "The top layer must contain the most tests",
   "The layers correspond to the seven testing principles"],
  "El número y el nombre de las capas pueden variar; también pueden usarse otros niveles de prueba.")
q("5.1.6", "Tests in the bottom layer of the test pyramid are typically:",
  "Small, isolated, fast, and check a small piece of functionality",
  ["Complex end-to-end business scenarios",
   "Manual usability tests",
   "Slow tests that need the whole system deployed"],
  "Los tests de la base son pequeños, aislados y rápidos, y comprueban una pieza pequeña, así que se necesitan muchos.")

# ---------------- FL-5.1.7 (K2) Testing quadrants (10) ----------------
q("5.1.7", "In the testing quadrants model, which quadrant contains technology-facing tests that critique the product, such as non-functional tests (except usability) and smoke tests?",
  "Q4",
  ["Q1", "Q2", "Q3"],
  "Q1: técnicos, apoyan al equipo (componente e integración de componentes). Q2: de negocio, apoyan al equipo (funcionales, ejemplos, historias, prototipos UX, API, simulaciones). Q3: de negocio, critican el producto (exploratoria, usabilidad, UAT). Q4: técnicos, critican el producto (smoke y no funcionales salvo usabilidad).")
q("5.1.7", "Which quadrant contains component tests and component integration tests that should be automated and included in the CI process?",
  "Q1",
  ["Q2", "Q3", "Q4"],
  "Q1 = orientado a la tecnología y de apoyo al equipo: pruebas de componente e integración de componentes, automatizadas y en CI.")
q("5.1.7", "Exploratory testing, usability testing and user acceptance testing belong to which quadrant?",
  "Q3 (business facing, critique the product)",
  ["Q1 (technology facing, support the team)",
   "Q2 (business facing, support the team)",
   "Q4 (technology facing, critique the product)"],
  "Q3 agrupa las pruebas orientadas al usuario que critican el producto, a menudo manuales: exploratoria, usabilidad y UAT.")
q("5.1.7", "Functional tests, examples, user story tests, user experience prototypes, API testing and simulations belong to which quadrant?",
  "Q2 (business facing, support the team)",
  ["Q1 (technology facing, support the team)",
   "Q3 (business facing, critique the product)",
   "Q4 (technology facing, critique the product)"],
  "Q2 comprueba los criterios de aceptación y puede ser manual o automatizado.")
q("5.1.7", "Which two viewpoints combine to form the four testing quadrants?",
  "Business facing vs technology facing, and support the team vs critique the product",
  ["Manual vs automated, and static vs dynamic",
   "Functional vs non-functional, and black-box vs white-box",
   "Early vs late, and cheap vs expensive"],
  "Los cuadrantes combinan dos ejes: orientado a negocio o a tecnología, y apoyo al equipo o crítica del producto.")
q("5.1.7", "Who defined the testing quadrants referenced in the syllabus?",
  "Brian Marick",
  ["Mike Cohn",
   "Glenford Myers",
   "Kent Beck"],
  "Los cuadrantes los definió Brian Marick (Marick 2003, Crispin 2008). La pirámide de pruebas es de Cohn.")
q("5.1.7", "Usability testing appears in which quadrant?",
  "Q3",
  ["Q4", "Q1", "Q2"],
  "La usabilidad está en Q3; Q4 contiene las no funcionales excepto la usabilidad.")
q("5.1.7", "How do the testing quadrants support test management?",
  "They help visualize that all appropriate test types and test levels are included in the SDLC",
  ["They define the exact number of test cases per sprint",
   "They replace risk analysis",
   "They determine the order of test execution"],
  "El modelo ayuda a visualizar que se incluyen todos los tipos y niveles de prueba adecuados, y que algunos tipos son más relevantes en ciertos niveles.")
q("5.1.7", "Tests in which quadrant check the acceptance criteria and can be manual or automated?",
  "Q2",
  ["Q1", "Q3", "Q4"],
  "Los tests de Q2 (de negocio, apoyo al equipo) comprueban los criterios de aceptación.")
q("5.1.7", "In the testing quadrants, what does \"critique the product\" mean?",
  "The tests measure the product's behavior against the expectations",
  ["The tests guide the development",
   "The tests are always manual",
   "The tests are written by critics outside the team"],
  "\"Support the team\" = guiar el desarrollo; \"critique the product\" = medir el comportamiento frente a las expectativas.")

# ---------------- FL-5.2.1 (K1) Risk level ----------------
q("5.2.1", "Risk level is determined by:",
  "Risk likelihood and risk impact",
  ["Number of test cases and test coverage",
   "Defect density and test duration",
   "Number of testers and project budget"],
  "El nivel de riesgo combina la probabilidad de que ocurra con el impacto (daño) si ocurre.")
q("5.2.1", "How is risk likelihood defined in the syllabus?",
  "The probability of the risk occurrence, greater than zero and less than one",
  ["The consequences of the risk occurrence",
   "The cost of mitigating the risk",
   "The number of times the risk has occurred before"],
  "La probabilidad del riesgo está entre 0 y 1 (excluidos); el impacto es el daño o las consecuencias.")
q("5.2.1", "What is a risk, according to the syllabus?",
  "A potential event, hazard, threat or situation whose occurrence causes an adverse effect",
  ["A defect that has already been found",
   "A failure in production",
   "A test case with high priority"],
  "Un riesgo es un evento, peligro, amenaza o situación potencial cuya ocurrencia causa un efecto adverso.")
q("5.2.1", "What does the risk level indicate?",
  "The higher the risk level, the more important is its treatment",
  ["The higher the risk level, the less testing is needed",
   "The risk level only matters for project risks",
   "The risk level is the number of affected requirements"],
  "El nivel de riesgo es una medida: cuanto mayor, más importante su tratamiento.")
q("5.2.1", "Risk impact is also known as:",
  "Harm",
  ["Likelihood",
   "Exposure time",
   "Coverage"],
  "El syllabus define el impacto del riesgo (harm) como las consecuencias de su ocurrencia.")
q("5.2.1", "Two risks have the same likelihood. Risk A would cause minor cosmetic issues; risk B would cause financial loss for customers. Which statement is correct?",
  "Risk B has a higher risk level because its impact is higher",
  ["Both risks have the same risk level because their likelihood is the same",
   "Risk A has a higher risk level because it is more visible",
   "Risk level cannot be compared without counting test cases"],
  "Con la misma probabilidad, el riesgo de mayor impacto tiene mayor nivel de riesgo.")

# ---------------- FL-5.2.2 (K2) Project vs product risks ----------------
q("5.2.2", "Which of the following is a PROJECT risk?",
  "The delivery of the test environment is delayed",
  ["The system calculates interest incorrectly",
   "The user interface is difficult to use",
   "The application contains a security vulnerability"],
  "Los riesgos de proyecto afectan a la gestión y el control: organizativos, de personas, técnicos y de proveedores. Los otros son riesgos de producto.")
q("5.2.2", "Which of the following is a PRODUCT risk?",
  "Inadequate response time of the system",
  ["Shortage of skilled testers",
   "Bankruptcy of a supporting supplier",
   "Inaccurate effort estimates"],
  "Los riesgos de producto están ligados a las características de calidad: funcionalidad, cálculos, errores en tiempo de ejecución, arquitectura, algoritmos, tiempo de respuesta, experiencia de usuario, seguridad.")
q("5.2.2", "Scope creep and poor tool support are examples of which kind of risk?",
  "Project risks (technical issues)",
  ["Product risks",
   "Safety risks",
   "Regulatory risks"],
  "Ampliación descontrolada del alcance y mal soporte de herramientas son riesgos de proyecto de tipo técnico.")
q("5.2.2", "What may happen when project risks occur?",
  "They may impact the project schedule, budget or scope",
  ["They directly cause failures in production",
   "They always cause physical damage",
   "They only affect the test team"],
  "Los riesgos de proyecto pueden afectar al calendario, al presupuesto o al alcance, y por tanto a la capacidad de cumplir objetivos.")
q("5.2.2", "Which of the following is a possible consequence of a product risk occurring?",
  "User dissatisfaction and loss of revenue, trust or reputation",
  ["A delay in the test environment delivery",
   "Conflicts within the team",
   "Inaccurate estimates"],
  "Consecuencias de riesgos de producto: insatisfacción del usuario, pérdida de ingresos o reputación, daños a terceros, altos costes de mantenimiento, sanciones penales e incluso daños físicos.")
q("5.2.2", "Communication problems and conflicts within the team are examples of:",
  "Project risks related to people issues",
  ["Product risks related to usability",
   "Product risks related to security",
   "Supplier issues"],
  "Son riesgos de proyecto de tipo \"personas\": habilidades insuficientes, conflictos, problemas de comunicación, falta de personal.")

# ---------------- FL-5.2.3 (K2) Product risk analysis ----------------
q("5.2.3", "What does product risk analysis consist of?",
  "Risk identification and risk assessment",
  ["Risk mitigation and risk monitoring",
   "Risk transfer and risk acceptance",
   "Defect reporting and defect fixing"],
  "El análisis de riesgos = identificación + evaluación. El control de riesgos = mitigación + monitorización.")
q("5.2.3", "How can the results of product risk analysis influence testing?",
  "They are used to determine the test scope, test levels, test types, test techniques and coverage to be achieved",
  ["They are used only to decide the release date",
   "They replace the need for test planning",
   "They determine which developer must fix each defect"],
  "Los resultados determinan alcance, niveles y tipos, técnicas y cobertura, esfuerzo, priorización y otras actividades además de las pruebas.")
q("5.2.3", "In the quantitative approach to risk assessment, how is the risk level calculated?",
  "As the multiplication of risk likelihood and risk impact",
  ["As the sum of all identified risks",
   "Using a risk matrix only",
   "As the number of test cases per risk"],
  "Cuantitativo: nivel = probabilidad × impacto. Cualitativo: se usa una matriz de riesgos.")
q("5.2.3", "Which technique can stakeholders use to identify risks?",
  "Brainstorming, workshops, interviews or cause-effect diagrams",
  ["Boundary value analysis",
   "Statement coverage",
   "Configuration management"],
  "El syllabus menciona lluvia de ideas, talleres, entrevistas y diagramas causa-efecto.")
q("5.2.3", "What is the goal of product risk analysis from a testing perspective?",
  "To provide awareness of product risk so that test effort is focused to minimize residual product risk",
  ["To eliminate all product risks before testing starts",
   "To avoid testing low-risk areas completely",
   "To replace the test plan with a risk register"],
  "El objetivo es enfocar el esfuerzo de prueba para minimizar el riesgo residual del producto, idealmente empezando pronto en el ciclo de vida.")
q("5.2.3", "Why is categorization of identified risks useful in risk assessment?",
  "Risks in the same category can usually be mitigated using a similar approach",
  ["Categorized risks do not need to be tested",
   "Categorization replaces risk likelihood",
   "Only categorized risks can be reported"],
  "Categorizar ayuda a asignar acciones de mitigación, porque los riesgos de una misma categoría suelen mitigarse de forma parecida.")

# ---------------- FL-5.2.4 (K2) Product risk control ----------------
q("5.2.4", "Which of the following is an example of mitigating product risks through testing?",
  "Applying the appropriate test techniques and coverage levels for the risk",
  ["Buying insurance against the consequences of the risk",
   "Accepting the risk without further action",
   "Preparing a contingency plan for when the risk occurs"],
  "Mitigación por pruebas: testers adecuados, nivel de independencia apropiado, revisiones y análisis estático, técnicas y cobertura apropiadas, tipos de prueba adecuados y prueba dinámica (incluida regresión).")
q("5.2.4", "Purchasing insurance to cover the consequences of a product risk is an example of:",
  "Risk transfer",
  ["Risk mitigation",
   "Risk acceptance",
   "Risk monitoring"],
  "Opciones de respuesta: mitigación por pruebas, aceptación, transferencia o plan de contingencia. Un seguro transfiere el riesgo.")
q("5.2.4", "What is the aim of risk monitoring?",
  "To ensure that mitigation actions are effective, obtain information to improve risk assessment and identify emerging risks",
  ["To identify risks for the first time",
   "To calculate the cost of testing",
   "To decide which developer caused the risk"],
  "La monitorización comprueba la eficacia de la mitigación, mejora la evaluación e identifica riesgos emergentes.")
q("5.2.4", "What does product risk control consist of?",
  "Risk mitigation and risk monitoring",
  ["Risk identification and risk assessment",
   "Risk transfer and defect management",
   "Test planning and test completion"],
  "El control de riesgos de producto = mitigación + monitorización.")
q("5.2.4", "Which action is a way to mitigate product risks by testing?",
  "Applying an appropriate level of independence of testing",
  ["Reducing the number of reviews",
   "Removing regression tests to save time",
   "Assigning the least experienced testers to the highest risks"],
  "Aplicar el nivel de independencia adecuado es una de las acciones de mitigación por pruebas.")
q("5.2.4", "A team decides to do nothing about a low-level product risk because the cost of mitigation outweighs the potential harm. Which response option is this?",
  "Risk acceptance",
  ["Risk transfer",
   "Risk mitigation by testing",
   "Contingency plan"],
  "Decidir no actuar ante un riesgo es aceptación del riesgo.")

# ---------------- FL-5.3.1 (K1) Metrics ----------------
q("5.3.1", "Which of the following is an example of a defect metric?",
  "Defect density",
  ["Test case implementation progress",
   "Mean time to failure",
   "Cost of testing"],
  "Métricas de defectos: número y prioridad de defectos encontrados/corregidos, densidad, porcentaje de detección. El tiempo medio hasta el fallo es de calidad de producto.")
q("5.3.1", "Requirements coverage and code coverage are examples of:",
  "Coverage metrics",
  ["Risk metrics",
   "Cost metrics",
   "Project progress metrics"],
  "El syllabus clasifica la cobertura de requisitos y de código como métricas de cobertura.")
q("5.3.1", "Which of the following is a product quality metric?",
  "Mean time to failure",
  ["Number of test cases run",
   "Task completion",
   "Organizational cost of quality"],
  "Métricas de calidad de producto: disponibilidad, tiempo de respuesta, tiempo medio hasta el fallo.")
q("5.3.1", "Residual risk level is an example of which type of metric?",
  "Risk metric",
  ["Coverage metric",
   "Test progress metric",
   "Defect metric"],
  "El nivel de riesgo residual es una métrica de riesgo.")
q("5.3.1", "Number of test cases run/not run and passed/failed are examples of:",
  "Test progress metrics",
  ["Product quality metrics",
   "Cost metrics",
   "Risk metrics"],
  "Métricas de progreso de prueba: avance de implementación de casos, preparación del entorno, casos ejecutados/no ejecutados, superados/fallidos, tiempo de ejecución.")
q("5.3.1", "Why are test metrics gathered?",
  "To show progress against the planned schedule and budget, the current quality of the test object and the effectiveness of test activities",
  ["To rank testers by performance",
   "To replace stakeholder communication",
   "To decide the programming language"],
  "Las métricas muestran el progreso frente a calendario y presupuesto, la calidad actual y la eficacia de las pruebas, y apoyan el control y el cierre.")

# ---------------- FL-5.3.2 (K2) Test reports ----------------
q("5.3.2", "Which content is typical of a test PROGRESS report?",
  "Progress against the test plan, impediments and workarounds, metrics, new and changed risks, and the testing planned for the next period",
  ["The final evaluation of product quality against the exit criteria for the whole project",
   "Lessons learned for future projects",
   "The archive of all testware at project end"],
  "El informe de progreso es periódico y apoya el control. La evaluación final, las lecciones aprendidas y los riesgos no mitigados van en el informe de finalización.")
q("5.3.2", "Which content is typical of a test COMPLETION report?",
  "Unmitigated risks, defects not fixed and lessons learned relevant to the testing",
  ["Testing planned for the next period",
   "Daily task assignments for testers",
   "The list of test cases to be executed tomorrow"],
  "Informe de finalización: resumen, evaluación frente al plan, desviaciones, impedimentos, métricas, riesgos no mitigados, defectos sin corregir y lecciones aprendidas.")
q("5.3.2", "When is a test completion report prepared?",
  "During test completion, when a project, test level or test type is complete and, ideally, its exit criteria have been met",
  ["Daily during test execution",
   "Before test planning starts",
   "Only when a critical defect is found"],
  "Se prepara en el cierre, cuando termina un proyecto, nivel o tipo de prueba, idealmente cumplidos los criterios de salida.")
q("5.3.2", "How does the audience influence test reporting?",
  "Different audiences require different information and influence the formality and frequency of reporting",
  ["All audiences must receive exactly the same report",
   "Reports should only be sent to testers",
   "The audience does not matter"],
  "Distintas audiencias necesitan información distinta: los informes de progreso dentro del equipo suelen ser frecuentes e informales; el de finalización sigue una plantilla y se hace una vez.")
q("5.3.2", "What is the main purpose of test progress reports?",
  "To support ongoing test control by providing enough information to modify the schedule, resources or test plan when needed",
  ["To archive testware",
   "To replace the test plan",
   "To evaluate tester performance"],
  "Los informes de progreso apoyan el control continuo y deben permitir cambiar el calendario, los recursos o el plan cuando haga falta.")
q("5.3.2", "What does the ISO/IEC/IEEE 29119-3 standard call test progress reports?",
  "Test status reports",
  ["Test incident reports",
   "Test logs",
   "Test summary plans"],
  "La norma 29119-3 llama a los informes de progreso test status reports.")

# ---------------- FL-5.3.3 (K2) Communicating test status ----------------
q("5.3.3", "Which of the following is an option for communicating the status of testing?",
  "Dashboards such as CI/CD dashboards, task boards and burn-down charts",
  ["Only formal written reports",
   "Only verbal communication",
   "Only the defect tracking tool"],
  "Opciones: comunicación verbal, dashboards, canales electrónicos (email, chat), documentación online e informes formales. Pueden combinarse.")
q("5.3.3", "For which teams may more formal communication be more appropriate?",
  "Distributed teams, where face-to-face communication is not always possible due to distance or time differences",
  ["Co-located teams working in the same room",
   "Teams with a single member",
   "Teams that do not use any tools"],
  "En equipos distribuidos, la comunicación más formal puede ser más adecuada por la distancia o las diferencias horarias.")
q("5.3.3", "How should the communication of test status be tailored?",
  "To the stakeholders, since different stakeholders are interested in different types of information",
  ["It should be identical for all stakeholders",
   "It should be decided only by the tool vendor",
   "It should contain only raw test logs"],
  "Cada stakeholder se interesa por información distinta, así que la comunicación debe adaptarse.")
q("5.3.3", "In the case of self-organizing teams, who decides the best means of communicating test status?",
  "The team itself",
  ["The tool vendor",
   "An external auditor",
   "Always the test manager"],
  "El syllabus indica que, en equipos autoorganizados, el propio equipo decide el mejor medio.")
q("5.3.3", "Email and chat are examples of which option for communicating test status?",
  "Electronic communication channels",
  ["Dashboards",
   "Formal test reports",
   "Online documentation"],
  "Email y chat son canales de comunicación electrónica.")
q("5.3.3", "Which statement about the means of communicating test status is correct?",
  "One or more options can be used, and the best means depends on factors such as test management concerns and regulatory standards",
  ["Only one option may be used per project",
   "Formal reports are always the best option",
   "Verbal communication is never acceptable"],
  "Se pueden combinar varias opciones; la mejor depende de la gestión de pruebas, la estrategia de la organización, la normativa o el propio equipo.")

# ---------------- FL-5.4.1 (K2) Configuration management (10) ----------------
q("5.4.1", "What is the main purpose of configuration management in testing?",
  "To identify, control and track work products such as test plans, test cases and test results as configuration items",
  ["To configure the test environment's hardware",
   "To decide which defects must be fixed before release",
   "To estimate the test effort"],
  "En testing, la gestión de la configuración es una disciplina para identificar, controlar y rastrear productos de trabajo como elementos de configuración.")
q("5.4.1", "What happens when a configuration item is approved for testing?",
  "It becomes a baseline and can only be changed through a formal change control process",
  ["It can be freely modified by anyone",
   "It is deleted from the repository",
   "It is automatically released to production"],
  "Al aprobarse para pruebas, el elemento se convierte en línea base y solo puede cambiarse mediante un control de cambios formal.")
q("5.4.1", "How does configuration management help reproduce previous test results?",
  "It keeps a record of changed items when a new baseline is created, making it possible to revert to a previous baseline",
  ["It stores only the latest version of each item",
   "It automatically re-executes all tests",
   "It deletes old test results"],
  "La gestión de la configuración registra los cambios al crear una nueva línea base y permite volver a una anterior para reproducir resultados.")
q("5.4.1", "For a complex configuration item such as a test environment, what does configuration management record?",
  "The items it consists of, their relationships and versions",
  ["Only the name of the environment",
   "Only the cost of the hardware",
   "Only the names of the testers who used it"],
  "Para elementos complejos registra sus componentes, sus relaciones y sus versiones.")
q("5.4.1", "To properly support testing, configuration management ensures that:",
  "All configuration items are uniquely identified, version controlled, tracked for changes and related to each other so that traceability can be maintained",
  ["All defects are fixed before release",
   "All tests are automated",
   "All requirements are approved by management"],
  "Garantiza identificación única, control de versiones, seguimiento de cambios y relación entre elementos (trazabilidad), y que el testware referencie sin ambigüedad la documentación y el software.")
q("5.4.1", "Where is automated configuration management normally included?",
  "In an automated DevOps pipeline implementing CI, continuous delivery and continuous deployment",
  ["Only in manual test procedures",
   "Only in the test completion report",
   "Only in the risk register"],
  "CI, entrega continua y despliegue continuo suelen implementarse en un pipeline DevOps automatizado, que normalmente incluye gestión de la configuración automatizada.")
q("5.4.1", "Which of the following are examples of work products managed as configuration items in testing?",
  "Test plans, test strategies, test conditions, test cases, test scripts, test results, test logs and test reports",
  ["Only the source code",
   "Only the requirements",
   "Only the defect reports"],
  "El syllabus enumera estos productos de prueba como posibles elementos de configuración.")
q("5.4.1", "What are \"test items\" in the context of configuration management?",
  "Individual parts of the test object",
  ["Items on a review checklist",
   "Rows in a decision table",
   "Entries in a risk register"],
  "El syllabus define los test items como partes individuales del objeto de prueba.")
q("5.4.1", "Which statement about the testware and configuration management is correct?",
  "All identified documentation and software items should be referenced unambiguously in testware",
  ["Testware should never reference software versions",
   "Testware is not subject to configuration management",
   "Only automated tests need to be referenced"],
  "La gestión de la configuración garantiza que la documentación y el software identificados se referencien sin ambigüedad en el testware.")
q("5.4.1", "A tester cannot reproduce a failure reported last month because nobody knows which build and test data were used. Which practice would have prevented this?",
  "Configuration management",
  ["Exploratory testing",
   "Risk transfer",
   "Planning Poker"],
  "La gestión de la configuración registra versiones y relaciones de los elementos (build, datos, entorno), lo que permite reproducir resultados anteriores.")

# ---------------- FL-5.5.1 (K3) Defect reports (handwritten scenarios) ----------------
q("5.5.1", "Which of the following should NOT be included in a defect report?",
  "An assessment of which developer is to blame for the defect",
  ["Steps to reproduce, with expected and actual results",
   "Severity and priority",
   "Identification of the test object and test environment"],
  "Un informe contiene identificador, título, fecha, organización y autor, objeto y entorno, contexto, descripción para reproducir, resultado esperado y real, severidad, prioridad, estado y referencias. Buscar culpables no aporta nada.")
q("5.5.1", "A defect report states: \"Title: Login fails. Steps: open app, log in. Result: error.\" Which essential information is MOST clearly missing to enable reproduction and resolution?",
  "The expected result, the test data used and the identification of the test object version and environment",
  ["The name of the tester's manager",
   "The tester's opinion about the developer",
   "The planned release date of the next version"],
  "Para reproducir y resolver hacen falta el resultado esperado, los datos usados (usuario, contraseña) y la versión del objeto y el entorno. Las otras opciones no ayudan a resolver.")
q("5.5.1", "A defect causes a typo in a rarely visited help page, but the CEO wants it fixed before tomorrow's demo. How should severity and priority be set?",
  "Low severity, high priority",
  ["High severity, low priority",
   "High severity, high priority",
   "Low severity, low priority"],
  "La severidad mide el impacto en stakeholders o requisitos (aquí bajo); la prioridad, la urgencia de corrección (aquí alta por la demo).")
q("5.5.1", "A defect corrupts customer data, but only in a feature that will not be released for six months. How should severity and priority typically be set?",
  "High severity, low priority",
  ["Low severity, high priority",
   "Low severity, low priority",
   "Severity and priority cannot be set until it is fixed"],
  "El impacto (corrupción de datos) es alto, pero la urgencia es baja porque la funcionalidad no se publicará pronto.")
q("5.5.1", "Which of the following is an objective of a typical defect report?",
  "Providing those responsible for handling the defect with sufficient information to resolve it",
  ["Measuring individual developer productivity",
   "Replacing the test plan",
   "Approving the release"],
  "Objetivos: dar información suficiente para resolver, permitir seguir la calidad del producto y aportar ideas de mejora de los procesos.")
q("5.5.1", "A tester reported an anomaly, but analysis showed the test expected result was wrong. Which status is the most appropriate for the defect report?",
  "Rejected",
  ["Re-opened",
   "Awaiting confirmation testing",
   "Deferred"],
  "Las anomalías reportadas pueden resultar no ser defectos (p. ej., un falso positivo). Rechazarlo es el estado adecuado. Ejemplos de estado: open, deferred, duplicate, waiting to be fixed, awaiting confirmation testing, re-opened, closed, rejected.")
q("5.5.1", "In which part of a defect report should you record \"test case TC-112 was being executed using boundary value test data during system testing\"?",
  "Context of the defect",
  ["Severity",
   "Status",
   "Title"],
  "El contexto incluye el caso de prueba ejecutado, la actividad, la fase del ciclo de vida y otra información relevante (técnica, checklist, datos).")
q("5.5.1", "Which of the following is the best title for a defect report?",
  "Checkout: total ignores 10% discount code for orders over €100",
  ["Bug",
   "Checkout is broken, developer did not test",
   "Something is wrong with prices sometimes"],
  "El título debe resumir brevemente la anomalía. Las otras opciones son vagas o acusatorias.")
q("5.5.1", "A defect fix has been delivered and the report is waiting for the tester to verify it. Which status fits best?",
  "Awaiting confirmation testing",
  ["Closed",
   "Duplicate",
   "Deferred"],
  "Tras entregarse el arreglo, el informe queda pendiente de la prueba de confirmación antes de cerrarse.")
q("5.5.1", "A tester finds that a new defect report describes exactly the same anomaly as an existing open report. What should be done?",
  "Mark the new report as a duplicate and reference the existing one",
  ["Close both reports",
   "Increase the severity of the original report",
   "Delete the original report"],
  "Un informe duplicado se marca como tal y se referencia al existente; \"duplicate\" es uno de los estados citados en el syllabus.")

# ---------------- FL-6.1.1 (K2) Tool support (10) ----------------
q("6.1.1", "Virtual machines and containerization tools that make test environments reproducible belong to which category?",
  "Tools supporting scalability and deployment standardization",
  ["Static testing tools",
   "Test management tools",
   "Non-functional testing tools"],
  "Categorías del syllabus: gestión de pruebas, prueba estática, diseño e implementación, ejecución y cobertura, prueba no funcional, DevOps, colaboración, escalabilidad y estandarización del despliegue, y cualquier otra herramienta que ayude.")
q("6.1.1", "A tool that executes automated tests and measures the code coverage achieved belongs to which category?",
  "Test execution and test coverage tools",
  ["Static testing tools",
   "Test management tools",
   "Collaboration tools"],
  "Las herramientas de ejecución y cobertura facilitan la ejecución automatizada y la medición de la cobertura.")
q("6.1.1", "Which category of tools increases test process efficiency by facilitating management of the SDLC, requirements, tests, defects and configuration?",
  "Test management tools",
  ["DevOps tools",
   "Test design and implementation tools",
   "Static testing tools"],
  "Las herramientas de gestión de pruebas facilitan la gestión del ciclo de vida, requisitos, pruebas, defectos y configuración.")
q("6.1.1", "Which category of tools allows the tester to perform tests that are difficult or impossible to perform manually, such as load testing?",
  "Non-functional testing tools",
  ["Collaboration tools",
   "Static testing tools",
   "Test management tools"],
  "Las herramientas de prueba no funcional permiten pruebas difíciles o imposibles de hacer manualmente.")
q("6.1.1", "Tools that support the delivery pipeline, workflow tracking, automated build processes and CI/CD belong to which category?",
  "DevOps tools",
  ["Test management tools",
   "Static testing tools",
   "Tools supporting scalability"],
  "Las herramientas DevOps apoyan el pipeline de entrega, el seguimiento del flujo, los builds automatizados y CI/CD.")
q("6.1.1", "Which category of tools facilitates the generation of test cases, test data and test procedures?",
  "Test design and test implementation tools",
  ["Test execution and coverage tools",
   "Collaboration tools",
   "DevOps tools"],
  "Las herramientas de diseño e implementación facilitan generar casos, datos y procedimientos de prueba.")
q("6.1.1", "Which category of tools supports testers in performing reviews and static analysis?",
  "Static testing tools",
  ["Non-functional testing tools",
   "Test execution tools",
   "DevOps tools"],
  "Las herramientas de prueba estática apoyan revisiones y análisis estático.")
q("6.1.1", "According to the syllabus, can a spreadsheet be considered a test tool?",
  "Yes, any tool that assists in testing, such as a spreadsheet, is a test tool in the context of testing",
  ["No, only commercial testing products are test tools",
   "No, only tools that execute tests are test tools",
   "Only if it is used for defect management"],
  "El syllabus dice explícitamente que cualquier herramienta que ayude a probar (p. ej., una hoja de cálculo) es una herramienta de prueba en ese contexto.")
q("6.1.1", "Which category of tools facilitates communication within the team?",
  "Collaboration tools",
  ["Test management tools",
   "DevOps tools",
   "Static testing tools"],
  "Las herramientas de colaboración facilitan la comunicación.")
q("6.1.1", "A team uses a tool to run the same performance test environment in identical containers on every developer's machine. Which tool category is this?",
  "Tools supporting scalability and deployment standardization",
  ["Collaboration tools",
   "Test design and test implementation tools",
   "Test management tools"],
  "Los contenedores para estandarizar y escalar despliegues de entornos pertenecen a esta categoría.")

# ---------------- FL-6.2.1 (K1) Benefits and risks of automation (10) ----------------
q("6.2.1", "Which of the following is a benefit of test automation?",
  "Time saved by reducing repetitive manual work, such as executing regression tests",
  ["No maintenance effort is needed once tests are written",
   "Automated tests find all defects",
   "The tool can replace test analysis and design"],
  "Beneficios: ahorro de trabajo manual repetitivo, prevención de errores humanos (consistencia y repetibilidad), evaluación más objetiva, acceso más fácil a la información, ejecución más rápida y más tiempo para diseñar mejores pruebas.")
q("6.2.1", "Which of the following is a risk of test automation?",
  "Unrealistic expectations about the benefits of the tool, including functionality and ease of use",
  ["More objective assessment through coverage measurement",
   "Faster feedback through earlier test execution",
   "More time for testers to design deeper tests"],
  "Riesgos: expectativas poco realistas, estimaciones inexactas, usar la herramienta cuando lo manual es más adecuado, confiar demasiado en ella, dependencia del proveedor, open source abandonado, incompatibilidad con la plataforma o incumplimiento normativo.")
q("6.2.1", "Which of the following is a risk of test automation?",
  "Inaccurate estimations of time, costs and effort required to introduce a tool and maintain test scripts",
  ["Prevention of simple human errors",
   "Reduced test execution times",
   "Easier access to information about testing"],
  "Subestimar el tiempo, el coste y el esfuerzo de introducir la herramienta y mantener los scripts es un riesgo típico.")
q("6.2.1", "Which of the following is a benefit of test automation?",
  "More objective assessment, such as coverage, and measures that are too complicated for humans to determine",
  ["Elimination of the need for human critical thinking",
   "Guaranteed compatibility with every development platform",
   "No dependency on any vendor"],
  "Una evaluación más objetiva y medidas demasiado complejas para hacerlas a mano son un beneficio de la automatización.")
q("6.2.1", "Relying on a tool too much, for example ignoring the need for human critical thinking, is:",
  "A risk of test automation",
  ["A benefit of test automation",
   "A test management activity",
   "A static testing technique"],
  "El syllabus lo cita expresamente como riesgo.")
q("6.2.1", "Which of the following is a risk of using an open-source test tool?",
  "It may be abandoned, so that no further updates are available",
  ["It always has hidden license fees",
   "It cannot be used for regression testing",
   "It cannot be integrated in CI"],
  "Un riesgo citado es que el software open source puede abandonarse o requerir actualizaciones frecuentes de sus componentes.")
q("6.2.1", "Prevention of simple human errors through greater consistency and repeatability is:",
  "A benefit of test automation",
  ["A risk of test automation",
   "A reason to avoid automation",
   "A configuration management activity"],
  "La consistencia y la repetibilidad (mismo orden, misma frecuencia) previenen errores humanos simples: es un beneficio.")
q("6.2.1", "Which of the following is a risk related to the tool vendor?",
  "The vendor may go out of business, retire the tool, sell it to another vendor or provide poor support",
  ["The vendor provides frequent upgrades",
   "The vendor offers training",
   "The vendor publishes documentation"],
  "La dependencia del proveedor es un riesgo: puede cerrar, retirar o vender la herramienta o dar mal soporte.")
q("6.2.1", "Using a test tool when manual testing is more appropriate is:",
  "A risk of test automation",
  ["A benefit of test automation",
   "A typical exit criterion",
   "A form of risk transfer"],
  "Usar una herramienta cuando la prueba manual es más adecuada aparece entre los riesgos de la automatización.")
q("6.2.1", "Which of the following is a benefit of test automation?",
  "Reduced test execution times, providing earlier defect detection, faster feedback and faster time to market",
  ["Choosing a tool that does not comply with safety standards",
   "Higher dependency on the tool vendor",
   "Automation tool incompatible with the development platform"],
  "Reducir los tiempos de ejecución da detección temprana, feedback más rápido y menor time to market. Las otras opciones son riesgos.")
