from qlib import q

# ---------------- FL-1.1.1 (K1) Typical test objectives ----------------
q("1.1.1", "Which of the following is a typical test objective?",
  "Evaluating work products such as requirements, user stories, designs and code",
  ["Proving that the software contains no defects",
   "Locating the cause of a failure in the code and removing it",
   "Executing every possible combination of inputs and preconditions"],
  "Evaluar productos de trabajo es uno de los objetivos típicos (1.1.1). Probar la ausencia de defectos es imposible (principio 1), localizar y eliminar la causa es depuración, y el testing exhaustivo es imposible (principio 2).")
q("1.1.1", "Which of the following is a typical test objective?",
  "Providing information to stakeholders so that they can make informed decisions",
  ["Assigning blame for defects to the responsible developer",
   "Replacing the need for code reviews",
   "Guaranteeing that the release date will be met"],
  "Proporcionar información a las partes interesadas para que tomen decisiones informadas (p. ej., la decisión de release) es un objetivo típico del testing.")
q("1.1.1", "Which statement about test objectives is correct?",
  "Test objectives can vary depending on the context, such as the test level, risks and the SDLC being followed",
  ["Test objectives are the same for every project and every test level",
   "The only test objective is to cause failures",
   "Test objectives are defined only after test execution has finished"],
  "El syllabus indica que los objetivos varían según el contexto: producto de trabajo probado, nivel de prueba, riesgos, ciclo de vida y factores de negocio (estructura corporativa, competencia, time to market).")
q("1.1.1", "Which of the following is a typical test objective?",
  "Verifying that a test object complies with contractual, legal and regulatory requirements",
  ["Writing the source code that satisfies the requirements",
   "Defining the product vision and business strategy",
   "Deploying the software to the production environment"],
  "Verificar el cumplimiento de requisitos contractuales, legales y regulatorios aparece literalmente entre los objetivos típicos del testing.")
q("1.1.1", "A team wants to build confidence that the test object works as users expect in its operational environment. Which typical test objective does this correspond to?",
  "Validating whether the test object is complete and works as expected by the stakeholders",
  ["Verifying whether specified requirements have been fulfilled",
   "Ensuring required coverage of a test object",
   "Reducing the effort needed for debugging"],
  "Comprobar que el sistema cumple las expectativas de los usuarios en su entorno es validación. Verificar requisitos especificados es verificación; ambos son objetivos distintos.")
q("1.1.1", "Which of the following is NOT one of the typical test objectives listed in the syllabus?",
  "Fixing the defects found during test execution",
  ["Causing failures and finding defects",
   "Ensuring required coverage of a test object",
   "Reducing the risk level of inadequate software quality"],
  "Corregir defectos es depuración, una actividad que no es de testing. Las otras tres opciones sí son objetivos típicos del testing.")

# ---------------- FL-1.1.2 (K2) Testing vs debugging ----------------
q("1.1.2", "Which activity is part of debugging rather than testing?",
  "Analysing the code to find the cause of a failure and removing it",
  ["Executing tests that trigger failures",
   "Re-running a failed test after a fix to check that it now passes",
   "Designing test cases from the requirements"],
  "El debugging reproduce el fallo, diagnostica (encuentra el defecto) y lo corrige. Ejecutar, re-ejecutar (confirmation testing) y diseñar tests son testing.")
q("1.1.2", "What is the typical sequence of the debugging process after dynamic testing has triggered a failure?",
  "Reproduce the failure, diagnose (find the defect), fix the defect",
  ["Fix the defect, reproduce the failure, report the defect",
   "Diagnose the defect, write a test case, close the defect report",
   "Report the failure, run regression tests, fix the defect"],
  "Según 1.1.2, el proceso típico de depuración es: reproducción del fallo, diagnóstico (encontrar el defecto) y corrección del defecto.")
q("1.1.2", "Static testing identifies a defect in a requirements document. Which statement about debugging in this situation is correct?",
  "Debugging only needs to remove the defect; reproduction and diagnosis are not needed",
  ["The failure must first be reproduced in a test environment",
   "Debugging is not possible because no failure has occurred",
   "The defect must be confirmed by dynamic testing before it can be removed"],
  "Cuando la prueba estática encuentra un defecto, la depuración consiste solo en eliminarlo: no hace falta reproducir ni diagnosticar, porque la prueba estática encuentra defectos directamente y no provoca fallos.")
q("1.1.2", "After a developer has fixed a defect, who should preferably perform the confirmation testing?",
  "The same person who performed the initial test",
  ["The developer who fixed the defect",
   "An external auditor",
   "The product owner"],
  "El syllabus indica que, preferiblemente, la prueba de confirmación la realiza la misma persona que hizo la prueba inicial.")
q("1.1.2", "Which statement best describes the difference between testing and debugging?",
  "Testing can trigger failures or directly find defects; debugging finds, analyses and removes the causes of failures",
  ["Testing removes defects; debugging finds them",
   "Testing is done only by testers; debugging is done only by testers",
   "Testing and debugging are two names for the same activity"],
  "Testing y debugging son actividades separadas: el testing provoca fallos (dinámico) o encuentra defectos (estático); la depuración busca las causas, las analiza y las elimina.")
q("1.1.2", "After a fix has passed confirmation testing, why might regression testing also be performed?",
  "To check whether the fix has caused failures in other parts of the test object",
  ["To reproduce the original failure once more",
   "To diagnose the root cause of the original defect",
   "To measure the time the developer needed to fix the defect"],
  "Tras la confirmación, la regresión comprueba que el arreglo no haya provocado fallos en otras partes del objeto de prueba.")

# ---------------- FL-1.2.1 (K2) Why testing is necessary ----------------
q("1.2.1", "Which of the following is a way in which testing contributes to the success of a project?",
  "Testing provides users with indirect representation on the development project",
  ["Testing directly removes defects from the code",
   "Testing guarantees that the product will be defect-free at release",
   "Testing replaces the need to involve stakeholders"],
  "Los testers representan indirectamente a los usuarios, ya que incluir a un grupo representativo de usuarios suele ser caro e inviable. El testing no elimina defectos (eso es depuración) ni garantiza la ausencia de defectos.")
q("1.2.1", "How does testing contribute to higher quality test objects?",
  "Indirectly: testing detects defects cost-effectively, and these defects can then be removed by debugging",
  ["Directly: testers fix the defects they find",
   "By proving that no defects remain after testing",
   "By replacing the need for quality assurance"],
  "El testing detecta defectos de forma rentable; se eliminan después mediante la depuración, que no es una actividad de testing. Por eso contribuye a la calidad de forma indirecta.")
q("1.2.1", "Which statement about testing's contribution to success is correct?",
  "Measures from testing contribute to decisions such as whether to move to the next SDLC phase or release",
  ["Testing results are not used for management decisions",
   "Testing contributes to success only when performed by the test team",
   "Testing is only necessary when required by regulations"],
  "El testing evalúa directamente la calidad del objeto de prueba en varias fases, y esas medidas apoyan decisiones como pasar de fase o hacer el release. Además, cualquier stakeholder puede usar habilidades de testing.")
q("1.2.1", "Why may testing be necessary even when the team is confident in the product?",
  "Testing may be required to meet contractual or legal requirements, or to comply with regulatory standards",
  ["Because testing proves that the product has no defects",
   "Because testing is the only way to improve development processes",
   "Because regulators require exhaustive testing of all inputs"],
  "El syllabus menciona que el testing puede ser obligatorio por requisitos contractuales, legales o normativos.")
q("1.2.1", "Testing is described in the syllabus as a form of quality control. Which statement about testing's contribution is correct?",
  "It helps achieve the agreed test objectives within scope, time, quality and budget constraints",
  ["It ensures that the project finishes ahead of schedule",
   "It is restricted to activities performed by the test team",
   "It focuses on improving the development process rather than the product"],
  "Como control de calidad, el testing ayuda a alcanzar los objetivos acordados dentro de las restricciones de alcance, tiempo, calidad y presupuesto. Su contribución no se limita al equipo de pruebas.")
q("1.2.1", "Why do testers often represent users during development instead of the users themselves?",
  "Involving a representative set of users is usually not possible due to high costs and lack of availability",
  ["Users are not allowed to see software before release",
   "Users cannot understand requirements",
   "Testers know the business better than users"],
  "El syllabus explica que la alternativa (incluir usuarios representativos) no suele ser posible por los altos costes y la falta de usuarios adecuados disponibles.")

# ---------------- FL-1.2.2 (K1) Testing and QA ----------------
q("1.2.2", "Which statement correctly describes the relationship between testing and quality assurance (QA)?",
  "Testing is product-oriented and corrective; QA is process-oriented and preventive",
  ["Testing and QA are two names for the same activity",
   "Testing is process-oriented; QA is product-oriented",
   "QA is only the responsibility of the test team"],
  "Testing: orientado al producto, correctivo, forma de control de calidad. QA: orientado al proceso, preventivo, responsabilidad de todos en el proyecto.")
q("1.2.2", "Who is responsible for quality assurance (QA) on a project?",
  "Everyone on the project",
  ["Only the test manager",
   "Only the QA department",
   "Only the developers"],
  "El syllabus dice que la QA se aplica a los procesos de desarrollo y de prueba y es responsabilidad de todos en el proyecto.")
q("1.2.2", "How are test results used in QA, as opposed to testing?",
  "In QA they provide feedback on how well the development and test processes are performing",
  ["In QA they are used to fix individual defects",
   "In QA they are ignored, as QA focuses only on processes",
   "In QA they are used to calculate the testers' bonuses"],
  "En testing los resultados se usan para corregir defectos; en QA dan feedback sobre el rendimiento de los procesos de desarrollo y prueba.")
q("1.2.2", "Which of the following is a form of quality control other than testing, according to the syllabus?",
  "Simulation and prototyping",
  ["Process improvement",
   "Root cause analysis",
   "Configuration management"],
  "El syllabus cita como otras formas de control de calidad los métodos formales (model checking y pruebas de corrección), la simulación y el prototipado.")
q("1.2.2", "QA works on which basic assumption?",
  "If a good process is followed correctly, it will generate a good product",
  ["If enough tests are executed, the product will be defect-free",
   "If testers are independent, all defects will be found",
   "If defects are fixed quickly, the process does not matter"],
  "La QA se basa en que un buen proceso seguido correctamente genera un buen producto; por eso se centra en implantar y mejorar procesos.")
q("1.2.2", "Which statement about testing and QA is correct?",
  "Testing is a major form of quality control",
  ["QA is a major form of testing",
   "Testing is a preventive, process-oriented approach",
   "QA applies only to the testing process"],
  "Según 1.2.2, el testing es una forma principal de control de calidad. La QA es preventiva, orientada al proceso, y se aplica tanto al desarrollo como a las pruebas.")

# ---------------- FL-1.2.3 (K2) Error, defect, failure, root cause ----------------
q("1.2.3", "A developer misunderstands a requirement and writes code that calculates VAT incorrectly. Months later a customer receives an invoice with the wrong total. What is the failure?",
  "The wrong total on the invoice the customer receives",
  ["The developer's misunderstanding of the requirement",
   "The incorrect VAT calculation in the source code",
   "The time pressure under which the developer worked"],
  "Error (equivocación) → defecto → fallo. El malentendido es el error, el cálculo incorrecto en el código es el defecto, y el total erróneo observado es el fallo. La presión de tiempo sería una posible causa raíz.")
q("1.2.3", "Which statement about defects and failures is correct?",
  "Some defects will always cause a failure if executed, while others only do so in specific circumstances, and some may never cause one",
  ["Every defect always results in a failure",
   "Failures can only be caused by defects in source code",
   "A defect in a requirements document cannot lead to defects in later work products"],
  "El syllabus indica que unos defectos siempre causan fallos al ejecutarse, otros solo en circunstancias concretas y otros nunca. Además, los defectos de productos tempranos suelen provocar defectos en productos posteriores.")
q("1.2.3", "Which of the following can cause a failure WITHOUT a defect introduced by a human error?",
  "Environmental conditions, such as radiation affecting firmware",
  ["A misunderstood user story",
   "A typo in the source code",
   "An incorrect formula in a design document"],
  "Los fallos también pueden deberse a condiciones ambientales, como radiación o campos electromagnéticos que causan defectos en el firmware.")
q("1.2.3", "What is a root cause?",
  "A fundamental reason for the occurrence of a problem, such as a situation that leads to an error",
  ["The first failure observed during system testing",
   "The line of code that contains the defect",
   "The test case that detected the failure"],
  "La causa raíz es la razón fundamental de un problema (p. ej., la situación que lleva a un error). Se identifica mediante análisis de causa raíz, y atacarla ayuda a prevenir defectos similares.")
q("1.2.3", "A team discovers that many defects were introduced because developers were never trained in a new framework. In terms of the syllabus, the lack of training is best described as:",
  "A root cause",
  ["A failure",
   "A defect",
   "A test condition"],
  "La falta de formación es una razón fundamental que lleva a errores humanos: una causa raíz. Corregirla puede prevenir defectos similares o reducir su frecuencia.")
q("1.2.3", "Where can defects be found, according to the syllabus?",
  "In documentation such as a requirements specification or a test script, in source code, or in supporting work products such as a build file",
  ["Only in executable source code",
   "Only in work products produced by developers",
   "Only in the production environment"],
  "Los defectos pueden estar en documentación (especificación de requisitos, script de prueba), en el código fuente o en productos de soporte, como un fichero de build.")

# ---------------- FL-1.3.1 (K2) Seven testing principles (10) ----------------
q("1.3.1", "A regression suite has run unchanged for two years. It rarely finds new defects, yet users keep reporting bugs in recently changed areas. Which testing principle explains this best?",
  "Tests wear out",
  ["Defects cluster together",
   "Absence-of-defects fallacy",
   "Early testing saves time and money"],
  "\"Tests wear out\": repetir los mismos tests los vuelve cada vez menos eficaces para encontrar defectos nuevos; hay que modificarlos o crear tests nuevos.")
q("1.3.1", "A system passes all its tests and has very few known defects, but users reject it because it does not support the way they actually work. Which principle does this illustrate?",
  "Absence-of-defects fallacy",
  ["Exhaustive testing is impossible",
   "Testing shows the presence, not the absence of defects",
   "Testing is context dependent"],
  "La falacia de la ausencia de defectos: verificar todos los requisitos y corregir todos los defectos no garantiza que el sistema satisfaga a los usuarios. Además de verificar hay que validar.")
q("1.3.1", "After a thorough test campaign no defects were found. Which conclusion is consistent with the testing principles?",
  "The probability of remaining defects is reduced, but the test object cannot be proven correct",
  ["The test object is proven to be defect-free",
   "Testing was ineffective and must be repeated",
   "No further testing will ever be needed"],
  "\"Testing shows the presence, not the absence of defects\": aunque no se encuentren defectos, el testing no puede demostrar que el objeto sea correcto; solo reduce la probabilidad de que queden defectos.")
q("1.3.1", "Which principle suggests using test techniques, test case prioritization and risk-based testing to focus test effort?",
  "Exhaustive testing is impossible",
  ["Tests wear out",
   "Defects cluster together",
   "Testing is context dependent"],
  "Como probarlo todo no es factible salvo en casos triviales, el syllabus recomienda técnicas, priorización y testing basado en riesgos para enfocar el esfuerzo.")
q("1.3.1", "Most of the defects in a system were found in two of its twenty modules. Which principle does this illustrate?",
  "Defects cluster together",
  ["Tests wear out",
   "Absence-of-defects fallacy",
   "Exhaustive testing is impossible"],
  "Agrupación de defectos: un número pequeño de componentes concentra la mayoría de defectos (principio de Pareto). Los clusters previstos y observados alimentan el testing basado en riesgos.")
q("1.3.1", "A safety-critical medical device and a marketing website are tested very differently. Which principle explains this?",
  "Testing is context dependent",
  ["Early testing saves time and money",
   "Defects cluster together",
   "Tests wear out"],
  "No existe un enfoque de prueba universal: el testing se hace de forma distinta en contextos distintos.")
q("1.3.1", "Which principle is supported by starting both static and dynamic testing as early as possible?",
  "Early testing saves time and money",
  ["Testing shows the presence, not the absence of defects",
   "Absence-of-defects fallacy",
   "Testing is context dependent"],
  "Los defectos eliminados pronto no causan defectos derivados y reducen el coste de la calidad; por eso conviene empezar pronto con la prueba estática y la dinámica.")
q("1.3.1", "In which situation can repeating exactly the same tests have a beneficial outcome, despite the 'tests wear out' principle?",
  "Automated regression testing",
  ["Exploratory testing of a new feature",
   "Searching for new defects in untested areas",
   "Acceptance testing with new users"],
  "El syllabus indica que, en algunos casos, repetir los mismos tests es beneficioso, por ejemplo en la regresión automatizada.")
q("1.3.1", "Which principle states that predicted and actual defect clusters are an important input for risk-based testing?",
  "Defects cluster together",
  ["Exhaustive testing is impossible",
   "Testing is context dependent",
   "Tests wear out"],
  "El principio 4 (los defectos se agrupan) menciona explícitamente que los clusters de defectos, previstos y observados, son una entrada importante para el testing basado en riesgos.")
q("1.3.1", "A team plans to test all combinations of 12 input fields, each with 10 possible values. Which principle shows this plan is not feasible?",
  "Exhaustive testing is impossible",
  ["Defects cluster together",
   "Early testing saves time and money",
   "Absence-of-defects fallacy"],
  "10^12 combinaciones no se pueden probar: el testing exhaustivo es imposible salvo en casos triviales. Hay que usar técnicas y priorización.")

# ---------------- FL-1.4.1 (K2) Test activities and tasks ----------------
q("1.4.1", "During which test activity are test conditions identified and prioritized?",
  "Test analysis",
  ["Test design",
   "Test implementation",
   "Test planning"],
  "El análisis responde a \"qué probar\": se analiza la base de prueba y se definen y priorizan condiciones de prueba. El diseño responde a \"cómo probar\".")
q("1.4.1", "Which test activity includes archiving testware for later reuse and creating a test completion report?",
  "Test completion",
  ["Test monitoring and test control",
   "Test execution",
   "Test implementation"],
  "El cierre ocurre en hitos (release, fin de iteración…): se archiva el testware útil, se recogen lecciones aprendidas, el entorno se deja en un estado acordado y se redacta el informe de finalización.")
q("1.4.1", "Which test activity elaborates test conditions into test cases, identifies coverage items and defines test data requirements?",
  "Test design",
  ["Test analysis",
   "Test implementation",
   "Test execution"],
  "El diseño (\"cómo probar\") convierte las condiciones en casos de prueba y otro testware (p. ej., test charters), identifica elementos de cobertura y define requisitos de datos y entorno.")
q("1.4.1", "In which test activity are test procedures organized into test suites, and the test environment built and verified?",
  "Test implementation",
  ["Test design",
   "Test planning",
   "Test completion"],
  "En la implementación se crea o adquiere el testware necesario para ejecutar (datos), se organizan procedimientos en suites, se crean scripts, se prepara el calendario de ejecución y se construye y verifica el entorno.")
q("1.4.1", "Which activity involves the ongoing checking of all test activities and comparing actual progress against the plan?",
  "Test monitoring",
  ["Test control",
   "Test analysis",
   "Test completion"],
  "La monitorización compara el progreso real con el plan; el control toma las acciones necesarias para cumplir los objetivos de prueba.")
q("1.4.1", "Which statement about the test activities is correct?",
  "Although they may appear sequential, they are often implemented iteratively or in parallel",
  ["They must always be performed strictly in sequence",
   "Test execution must start before test analysis",
   "Test planning is only performed once, at the end of the project"],
  "El syllabus indica que, aunque parezcan seguir una secuencia lógica, las actividades suelen realizarse de forma iterativa o en paralelo y deben adaptarse al sistema y al proyecto.")

# ---------------- FL-1.4.2 (K2) Test process in context ----------------
q("1.4.2", "Which of the following is a contextual factor that influences how testing is carried out?",
  "The business domain, including the criticality of the test object and legal regulations",
  ["The colour scheme of the user interface",
   "The personal preferences of the test tool vendor",
   "The number of meeting rooms available"],
  "Factores de contexto: stakeholders, miembros del equipo, dominio de negocio, factores técnicos, restricciones del proyecto, factores organizativos, ciclo de vida y herramientas.")
q("1.4.2", "Which aspects of testing can be impacted by contextual factors such as stakeholders, project constraints and tools?",
  "The test strategy, test techniques used, degree of test automation and required coverage",
  ["Only the number of testers in the team",
   "Only the choice of defect management tool",
   "Nothing; the test process is the same in every context"],
  "Los factores de contexto afectan a la estrategia, las técnicas, el grado de automatización, la cobertura requerida, el nivel de detalle del testware y el reporting.")
q("1.4.2", "Team members' skills, experience and availability are an example of which type of contextual factor?",
  "Team members",
  ["Technical factors",
   "Organizational factors",
   "Project constraints"],
  "El syllabus lista \"Team members (skills, knowledge, level of experience, availability, training needs)\" como factor de contexto propio.")
q("1.4.2", "Scope, time, budget and resources are listed in the syllabus as examples of which contextual factor?",
  "Project constraints",
  ["Business domain",
   "Stakeholders",
   "Software development lifecycle"],
  "Alcance, tiempo, presupuesto y recursos son restricciones del proyecto.")
q("1.4.2", "Why does the test process depend on its context?",
  "Testing is an integral part of the organization's development processes and is funded by stakeholders to help fulfill their business needs",
  ["Because international standards forbid a common test process",
   "Because testers decide alone how testing is performed",
   "Because the test process only depends on the tool used"],
  "El testing no se hace aislado: forma parte de los procesos de desarrollo de la organización y lo financian los stakeholders para cubrir sus necesidades de negocio.")
q("1.4.2", "The type of software, product architecture and technology used are examples of which contextual factor?",
  "Technical factors",
  ["Organizational factors",
   "Business domain",
   "Tools"],
  "Tipo de software, arquitectura del producto y tecnología usada son factores técnicos.")

# ---------------- FL-1.4.3 (K2) Testware ----------------
q("1.4.3", "Which work product is typically produced by test implementation?",
  "Test procedures and automated test scripts",
  ["Test completion report",
   "Prioritized test conditions",
   "Risk register"],
  "Productos de implementación: procedimientos, scripts manuales y automatizados, suites, datos, calendario de ejecución y elementos del entorno (stubs, drivers, simuladores, virtualización de servicios).")
q("1.4.3", "Which of the following is a work product of test analysis?",
  "Prioritized test conditions, such as acceptance criteria",
  ["Test logs",
   "Test charters",
   "Test execution schedule"],
  "El análisis produce condiciones de prueba (priorizadas), como los criterios de aceptación, y reportes de defectos de la base de prueba. Los test charters son de diseño; los logs, de ejecución.")
q("1.4.3", "Stubs, drivers, simulators and service virtualizations are examples of:",
  "Test environment items produced during test implementation",
  ["Test design work products",
   "Test completion work products",
   "Test planning work products"],
  "El syllabus los cita como ejemplos de elementos del entorno de prueba, que son productos de la implementación.")
q("1.4.3", "Which work products are typical outputs of test execution?",
  "Test logs and defect reports",
  ["Test plans and risk registers",
   "Test cases and coverage items",
   "Lessons learned and change requests"],
  "La ejecución produce logs de prueba y reportes de defectos.")
q("1.4.3", "Test cases, test charters, coverage items and test data requirements are typical work products of which activity?",
  "Test design",
  ["Test analysis",
   "Test implementation",
   "Test monitoring and test control"],
  "Todos ellos son productos del diseño de pruebas (\"cómo probar\").")
q("1.4.3", "Which of the following is a typical work product of test planning?",
  "Entry criteria and exit criteria",
  ["Test progress reports",
   "Test suites",
   "Test logs"],
  "Productos de planificación: plan de prueba, calendario, registro de riesgos y criterios de entrada y salida. Los informes de progreso son de monitorización y control.")

# ---------------- FL-1.4.4 (K2) Traceability ----------------
q("1.4.4", "What is a key benefit of maintaining traceability between the test basis, testware, test results and defects?",
  "It supports coverage evaluation and makes it possible to determine the impact of changes",
  ["It removes the need for regression testing",
   "It guarantees that all defects will be found",
   "It makes reviews of the test basis unnecessary"],
  "La trazabilidad permite evaluar la cobertura, determinar el impacto de los cambios, facilita auditorías y ayuda a cumplir criterios de gobierno de TI.")
q("1.4.4", "Traceability of test results to risks can be used to:",
  "Evaluate the level of residual risk in a test object",
  ["Estimate the development effort",
   "Choose the test automation tool",
   "Define the user stories"],
  "El syllabus da este ejemplo: trazar resultados a riesgos permite evaluar el riesgo residual del objeto de prueba.")
q("1.4.4", "Traceability of test cases to requirements can be used to:",
  "Verify that the requirements are covered by test cases",
  ["Calculate the defect density of the code",
   "Decide which developer should fix a defect",
   "Measure the performance of the system"],
  "Trazar casos de prueba a requisitos permite verificar que los requisitos están cubiertos.")
q("1.4.4", "How does good traceability help test reporting?",
  "It makes test progress and completion reports easier to understand by including the status of test basis elements",
  ["It removes the need for test reports",
   "It allows reports to be produced without test execution",
   "It hides technical details from all stakeholders"],
  "Incluir el estado de los elementos de la base de prueba hace los informes más comprensibles y ayuda a comunicar aspectos técnicos a los stakeholders.")
q("1.4.4", "Which statement about traceability and coverage criteria is correct?",
  "It is very useful if measurable coverage criteria are defined in the test basis, as they can act as key performance indicators",
  ["Coverage criteria cannot be defined when traceability exists",
   "Traceability is only needed for white-box coverage",
   "Coverage criteria should be defined only after the release"],
  "Una trazabilidad precisa apoya la evaluación de la cobertura; los criterios de cobertura medibles pueden funcionar como KPIs que indican hasta qué punto se cumplen los objetivos.")
q("1.4.4", "Besides evaluating coverage, which of the following is a benefit of good traceability mentioned in the syllabus?",
  "It facilitates audits and helps meet IT governance criteria",
  ["It reduces the number of test levels needed",
   "It allows testers to skip test analysis",
   "It replaces configuration management"],
  "La buena trazabilidad facilita auditorías, ayuda a cumplir criterios de gobierno de TI y da información sobre la calidad del producto, la capacidad del proceso y el avance del proyecto.")

# ---------------- FL-1.4.5 (K2) Roles in testing ----------------
q("1.4.5", "The test management role mainly focuses on which activities?",
  "Test planning, test monitoring, test control and test completion",
  ["Test analysis, test design, test implementation and test execution",
   "Coding, debugging and deployment",
   "Requirements elicitation and user story writing"],
  "El rol de gestión de pruebas asume la responsabilidad global del proceso y se centra en planificación, monitorización, control y cierre.")
q("1.4.5", "The testing role mainly focuses on which activities?",
  "Test analysis, test design, test implementation and test execution",
  ["Test planning, test monitoring, test control and test completion",
   "Release planning and budgeting",
   "Recruiting and training testers"],
  "El rol de testing asume la responsabilidad del aspecto de ingeniería (técnico) de las pruebas: análisis, diseño, implementación y ejecución.")
q("1.4.5", "Which statement about the roles in testing is correct?",
  "One person may take on the testing role and the test management role at the same time",
  ["The test management role can only be performed by a test manager",
   "The testing role is only allowed in sequential lifecycles",
   "In Agile teams, test management tasks are never handled by the team"],
  "El syllabus indica que distintas personas pueden asumir los roles en distintos momentos, y que una misma persona puede tener ambos a la vez.")
q("1.4.5", "In Agile software development, how may test management tasks be handled?",
  "Some may be handled by the Agile team, while tasks spanning several teams may be done by test managers outside the team",
  ["They are always performed by an external test manager",
   "They are eliminated because Agile teams do not plan",
   "They are always performed by the product owner"],
  "En ágil, parte de las tareas de gestión de pruebas las asume el equipo; las que abarcan varios equipos o toda la organización pueden hacerlas test managers externos al equipo.")
q("1.4.5", "Who can perform the test management role, according to the syllabus?",
  "A team leader, a test manager or a development manager, among others",
  ["Only a certified test manager",
   "Only the most senior tester",
   "Only the project sponsor"],
  "El syllabus da como ejemplos de quién puede desempeñar el rol de gestión: un líder de equipo, un test manager o un responsable de desarrollo.")
q("1.4.5", "Which responsibility belongs to the testing role rather than the test management role?",
  "Designing test cases from test conditions",
  ["Creating the test plan",
   "Taking control actions when testing deviates from the plan",
   "Writing the test completion report"],
  "Diseñar casos de prueba es una tarea de ingeniería (rol de testing). Planificar, controlar y cerrar corresponden al rol de gestión.")

# ---------------- FL-1.5.1 (K2) Generic skills ----------------
q("1.5.1", "Why are good communication skills especially important for testers?",
  "Testers are often the bearers of bad news, and test results may be perceived as criticism of the product and its author",
  ["Testers are responsible for writing all project documentation",
   "Communication skills replace the need for technical knowledge",
   "Testers must negotiate the project budget"],
  "Los testers suelen dar malas noticias, y comunicar resultados puede percibirse como crítica. El sesgo de confirmación dificulta aceptar información contraria; hay que comunicar los defectos de forma constructiva.")
q("1.5.1", "Which generic skill helps a tester increase the efficiency of testing, for example by using appropriate test tools?",
  "Technical knowledge",
  ["Domain knowledge",
   "Curiosity",
   "Active listening"],
  "El syllabus asocia el conocimiento técnico con la eficiencia (p. ej., usar herramientas adecuadas). El conocimiento de testing, el pensamiento analítico y la creatividad aumentan la eficacia.")
q("1.5.1", "Which generic skill enables a tester to understand and communicate with end users and business representatives?",
  "Domain knowledge",
  ["Technical knowledge",
   "Thoroughness",
   "Testing knowledge"],
  "El conocimiento del dominio permite entender a los usuarios finales y a negocio y comunicarse con ellos.")
q("1.5.1", "Thoroughness, carefulness, curiosity and attention to detail help testers mainly to:",
  "Identify defects, especially those that are difficult to find",
  ["Estimate the test effort precisely",
   "Negotiate with the tool vendor",
   "Avoid writing defect reports"],
  "Según 1.5.1, ser minucioso, cuidadoso, curioso, metódico y atento al detalle sirve para encontrar defectos, especialmente los difíciles de detectar.")
q("1.5.1", "How should information about defects and failures be communicated?",
  "In a constructive way",
  ["Only in writing, never verbally",
   "Only to the developer who caused it",
   "Including the name of the person to blame"],
  "Para mejorar la percepción del testing como actividad destructiva, la información sobre defectos y fallos debe comunicarse de forma constructiva.")
q("1.5.1", "Which cognitive bias can make it difficult for people to accept information that disagrees with their current beliefs, such as a defect report?",
  "Confirmation bias",
  ["Anchoring bias",
   "Survivorship bias",
   "Availability bias"],
  "El syllabus menciona el sesgo de confirmación: puede dificultar aceptar información que contradice lo que se cree.")

# ---------------- FL-1.5.2 (K1) Whole team approach (10) ----------------
q("1.5.2", "Which statement best describes the whole team approach?",
  "Any team member with the necessary knowledge and skills can perform any task, and everyone is responsible for quality",
  ["Testers alone are responsible for product quality",
   "Developers do only component testing and testers do all other testing",
   "Business representatives write all acceptance tests on their own"],
  "En el enfoque de equipo completo cualquiera con los conocimientos necesarios puede hacer cualquier tarea y todos son responsables de la calidad.")
q("1.5.2", "From which practice does the whole team approach originate?",
  "Extreme Programming (XP)",
  ["The V-model",
   "PRINCE2",
   "ITIL"],
  "El syllabus indica que el enfoque de equipo completo procede de Extreme Programming.")
q("1.5.2", "Which of the following is an advantage of the whole team approach?",
  "It improves team dynamics and enhances communication and collaboration within the team",
  ["It removes the need for testers in the team",
   "It guarantees a high level of test independence",
   "It eliminates the need for acceptance testing"],
  "Ventajas: mejora la dinámica del equipo, la comunicación y la colaboración, y crea sinergia al aprovechar las distintas habilidades.")
q("1.5.2", "In the whole team approach, how do testers collaborate with business representatives?",
  "They help them create suitable acceptance tests",
  ["They write the business requirements for them",
   "They approve the business budget",
   "They replace them in sprint reviews"],
  "Los testers ayudan a los representantes de negocio a crear pruebas de aceptación adecuadas, y con los desarrolladores acuerdan la estrategia de prueba y la automatización.")
q("1.5.2", "In which situation may the whole team approach NOT be appropriate?",
  "Safety-critical development, where a high level of test independence may be needed",
  ["A small co-located Agile team",
   "A team using continuous integration",
   "A project with business representatives available"],
  "El syllabus señala que en contextos como los de seguridad crítica puede necesitarse una alta independencia de las pruebas, así que el enfoque de equipo completo puede no ser adecuado.")
q("1.5.2", "Why do team members share the same workspace in the whole team approach?",
  "Co-location, physical or virtual, facilitates communication and interaction",
  ["It reduces office costs",
   "It allows managers to monitor individual productivity",
   "It is required by ISO standards"],
  "Compartir espacio (físico o virtual) facilita la comunicación y la interacción.")
q("1.5.2", "In the whole team approach, testers work with developers mainly to:",
  "Agree on the test strategy and decide on test automation approaches",
  ["Approve every line of code before it is committed",
   "Take over all debugging tasks",
   "Write the developers' performance reviews"],
  "Con los desarrolladores, los testers acuerdan la estrategia de prueba y deciden los enfoques de automatización; así transfieren conocimiento de testing al equipo.")
q("1.5.2", "Who is responsible for quality in the whole team approach?",
  "Everyone in the team",
  ["The tester",
   "The product owner",
   "The Scrum Master"],
  "Clave del enfoque de equipo completo: todos son responsables de la calidad.")
q("1.5.2", "How can testers influence the development of the product in the whole team approach?",
  "By transferring testing knowledge to other team members",
  ["By vetoing any change to the requirements",
   "By working in isolation from the developers",
   "By postponing testing until the end of the iteration"],
  "Al trabajar estrechamente con el equipo, los testers transfieren conocimiento de pruebas e influyen en el desarrollo del producto.")
q("1.5.2", "The whole team approach builds upon which essential tester skill?",
  "The ability to work effectively in a team context and contribute positively to team goals",
  ["The ability to work independently of the developers",
   "The ability to write test automation code",
   "The ability to estimate test effort accurately"],
  "El syllabus dice que el enfoque de equipo completo se apoya en la habilidad de trabajar eficazmente en equipo y contribuir a sus objetivos.")

# ---------------- FL-1.5.3 (K2) Independence of testing ----------------
q("1.5.3", "Which of the following is a potential DRAWBACK of independent testing?",
  "Developers may lose a sense of responsibility for quality",
  ["Independent testers tend to find different kinds of failures than developers",
   "Independent testers can challenge assumptions made by stakeholders",
   "Independent testers are affected by different cognitive biases than the author"],
  "Inconvenientes: aislamiento del equipo, problemas de comunicación o relación adversarial, desarrolladores que pierden el sentido de responsabilidad sobre la calidad, y testers vistos como cuello de botella.")
q("1.5.3", "Which level of independence applies when a work product is tested by testers from outside the author's team but within the same organization?",
  "High independence",
  ["No independence",
   "Some independence",
   "Very high independence"],
  "Autor: sin independencia. Compañeros del mismo equipo: alguna. Testers de fuera del equipo dentro de la organización: alta. Testers externos a la organización: muy alta.")
q("1.5.3", "What is the main benefit of independence of testing?",
  "Independent testers are likely to recognize different kinds of failures and defects because of their different backgrounds and biases",
  ["Independent testers do not need any knowledge of the system",
   "Independent testing removes the need for developer testing",
   "Independent testers can fix defects faster"],
  "La principal ventaja es que, por sus distintos conocimientos, perspectivas y sesgos, los testers independientes detectan tipos de defectos distintos a los de los desarrolladores.")
q("1.5.3", "For most projects, which approach to independence is usually best?",
  "Testing with multiple levels of independence, e.g., developers doing component testing and business representatives doing acceptance testing",
  ["Only very high independence for all test levels",
   "Only testing by the author, for efficiency",
   "No testing by developers at all"],
  "El syllabus recomienda varios niveles de independencia: desarrolladores en componente e integración de componentes, el equipo de pruebas en sistema e integración de sistemas, y negocio en aceptación.")
q("1.5.3", "Which statement about independence and familiarity is correct?",
  "Independence is not a replacement for familiarity; developers can efficiently find many defects in their own code",
  ["Authors are never able to find defects in their own work",
   "Familiarity with the code always reduces the number of defects found",
   "Independent testers should avoid learning about the system"],
  "La independencia no sustituye a la familiaridad: los desarrolladores pueden encontrar eficientemente muchos defectos en su propio código.")
q("1.5.3", "Testing performed by an external company contracted by the organization is an example of:",
  "Very high independence",
  ["Some independence",
   "High independence",
   "No independence"],
  "Testers de fuera de la organización = independencia muy alta.")
