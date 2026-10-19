from qlib import q

# ---------------- FL-3.1.1 (K1) Work products examinable by static testing ----------------
q("3.1.1", "Which of the following work products can be examined using static testing?",
  "Contracts, test plans, product backlog items and source code",
  ["Only source code",
   "Only requirements specifications",
   "Only executable binaries"],
  "Casi cualquier producto de trabajo puede examinarse con prueba estática: especificaciones, código, planes y casos de prueba, backlog, test charters, documentación del proyecto, contratos y modelos.")
q("3.1.1", "Which work product is NOT appropriate for static testing according to the syllabus?",
  "Third-party executable code that should not be analysed for legal reasons",
  ["A test charter",
   "A user story with acceptance criteria",
   "An architecture model"],
  "No son adecuados los productos difíciles de interpretar por personas y que no deben analizarse con herramientas (p. ej., código ejecutable de terceros por motivos legales).")
q("3.1.1", "What do work products need in order to be examined by static analysis (rather than by a review)?",
  "A structure against which they can be checked, such as models, code or text with a formal syntax",
  ["A signature from the product owner",
   "At least 100 lines of content",
   "An executable form"],
  "Para una revisión basta con que el producto pueda leerse y entenderse; para el análisis estático necesita una estructura comprobable (modelos, código o texto con sintaxis formal).")
q("3.1.1", "Which of the following can be the subject of a review?",
  "Any work product that can be read and understood",
  ["Only work products with a formal syntax",
   "Only code that compiles",
   "Only documents approved by management"],
  "Cualquier producto de trabajo que pueda leerse y entenderse puede ser objeto de una revisión.")
q("3.1.1", "Spelling checkers and readability tools are examples of:",
  "Static analysis tools",
  ["Dynamic testing tools",
   "Test execution tools",
   "Performance testing tools"],
  "El syllabus cita los correctores ortográficos y las herramientas de legibilidad como ejemplos de herramientas de análisis estático.")
q("3.1.1", "Which activities can be used to ensure that user stories meet defined criteria such as the Definition of Ready?",
  "Example mapping, collaborative user story writing and backlog refinement sessions",
  ["Performance testing and load testing",
   "Component testing and debugging",
   "Beta testing and alpha testing"],
  "Testers, negocio y desarrolladores colaboran en example mapping, escritura colaborativa de historias y refinamiento del backlog para que las historias cumplan criterios como la Definition of Ready.")

# ---------------- FL-3.1.2 (K2) Value of static testing ----------------
q("3.1.2", "Which statement about the value of static testing is correct?",
  "It can detect defects that cannot be detected by dynamic testing, such as unreachable code",
  ["It requires executing the code",
   "It can only find failures, not defects",
   "It is always more expensive overall than not performing reviews"],
  "La prueba estática detecta defectos que la dinámica no puede (código inalcanzable, patrones de diseño no implementados como se esperaba, defectos en productos no ejecutables).")
q("3.1.2", "Why are the overall project costs usually lower when reviews are performed, even though reviews can be costly to implement?",
  "Less time and effort is needed to fix defects later in the project",
  ["Reviews replace all dynamic testing",
   "Reviews reduce the number of requirements",
   "Reviews eliminate the need for test automation"],
  "Aunque las revisiones cuestan, el coste total suele ser menor porque se gasta menos en corregir defectos más adelante.")
q("3.1.2", "Why does the syllabus recommend involving a wide variety of stakeholders in static testing?",
  "Static testing performed early creates a shared understanding and improves communication between stakeholders",
  ["Because static testing requires many people to execute the code",
   "Because only stakeholders can operate static analysis tools",
   "Because it removes the need for acceptance testing"],
  "Al hacerse pronto, la prueba estática crea un entendimiento compartido y mejora la comunicación, por eso conviene involucrar a muchos stakeholders.")
q("3.1.2", "How can static testing help stakeholders with respect to requirements?",
  "By verifying the documented requirements, stakeholders can make sure they describe their actual needs",
  ["By automatically generating code from requirements",
   "By measuring the performance of the requirements",
   "By replacing requirements with test cases"],
  "Verificar los requisitos documentados permite a los stakeholders comprobar que describen sus necesidades reales.")
q("3.1.2", "Which statement about static analysis is correct?",
  "Certain code defects can be detected more efficiently with static analysis than with dynamic testing",
  ["Static analysis needs test cases to be written first",
   "Static analysis can only be done manually",
   "Static analysis is only used to measure performance efficiency"],
  "El análisis estático detecta ciertos defectos de código con más eficiencia, sin necesidad de casos de prueba, y suele integrarse en CI. También se usa para evaluar mantenibilidad y seguridad.")
q("3.1.2", "Static testing in the earliest phases of the SDLC fulfils which testing principle?",
  "Early testing saves time and money",
  ["Tests wear out",
   "Exhaustive testing is impossible",
   "Absence-of-defects fallacy"],
  "La prueba estática puede detectar defectos en las fases más tempranas, cumpliendo el principio de prueba temprana.")

# ---------------- FL-3.1.3 (K2) Static vs dynamic testing ----------------
q("3.1.3", "Which type of defect is typically easier and/or cheaper to find with static testing than with dynamic testing?",
  "Deviations from coding standards, such as naming conventions",
  ["A memory leak that appears only under sustained load",
   "Slow response times with many concurrent users",
   "A run-time failure when calling a third-party API"],
  "Típicos de la prueba estática: defectos en requisitos, de diseño, ciertos de código (variables sin definir, código inalcanzable o duplicado), desviaciones de estándares, interfaces mal especificadas, ciertas vulnerabilidades y huecos de cobertura de la base de prueba.")
q("3.1.3", "Which statement correctly contrasts static and dynamic testing?",
  "Static testing finds defects directly, while dynamic testing causes failures from which the defects are determined by analysis",
  ["Static testing causes failures; dynamic testing finds defects directly",
   "Both can only be applied to executable work products",
   "Dynamic testing can be applied to non-executable work products"],
  "La prueba estática encuentra defectos directamente; la dinámica provoca fallos y el defecto se determina después con análisis.")
q("3.1.3", "Which quality characteristic is typically measured by static testing rather than dynamic testing?",
  "Maintainability",
  ["Performance efficiency",
   "Response time under load",
   "Throughput"],
  "La prueba estática mide características que no dependen de ejecutar código (p. ej., mantenibilidad); la dinámica, las que sí (p. ej., eficiencia de desempeño).")
q("3.1.3", "Mismatched number, type or order of parameters in an interface specification is an example of a defect that is:",
  "Typically easier to find through static testing",
  ["Only detectable through performance testing",
   "Only detectable in production",
   "Impossible to detect before acceptance testing"],
  "El syllabus cita las especificaciones de interfaz incorrectas como defectos que es más fácil y barato encontrar con prueba estática.")
q("3.1.3", "Why may static testing more easily detect defects on rarely executed code paths?",
  "It does not depend on executing those paths, which are hard to reach with dynamic testing",
  ["It executes all paths automatically",
   "It uses production data",
   "It requires 100% branch coverage"],
  "La prueba estática no necesita ejecutar el código, así que encuentra más fácilmente defectos en caminos raros o difíciles de alcanzar dinámicamente.")
q("3.1.3", "Which statement about static and dynamic testing is correct?",
  "They complement each other and have similar objectives, but some defect types can only be found by one of them",
  ["Static testing makes dynamic testing unnecessary",
   "Dynamic testing makes static testing unnecessary",
   "They have completely different objectives"],
  "Son prácticas complementarias con objetivos similares, pero hay tipos de defectos que solo puede detectar una u otra.")

# ---------------- FL-3.2.1 (K1) Early and frequent stakeholder feedback ----------------
q("3.2.1", "What is a benefit of early and frequent stakeholder feedback?",
  "It allows early communication of potential quality problems",
  ["It removes the need for test planning",
   "It guarantees that requirements never change",
   "It replaces acceptance testing"],
  "El feedback temprano y frecuente comunica pronto posibles problemas de calidad y evita malentendidos sobre los requisitos.")
q("3.2.1", "What can happen if there is little stakeholder involvement during the SDLC?",
  "The product might not meet the stakeholders' original or current vision, causing costly rework or even project failure",
  ["The product will be delivered earlier",
   "The number of defects found by testers will increase",
   "Testing will become unnecessary"],
  "Con poca participación, el producto puede no cumplir la visión del stakeholder: retrabajo costoso, plazos incumplidos, búsqueda de culpables o incluso fracaso del proyecto.")
q("3.2.1", "How does frequent stakeholder feedback help the development team?",
  "It helps them focus on the features that deliver the most value and have the most positive impact on identified risks",
  ["It lets them skip writing tests",
   "It allows them to ignore non-functional requirements",
   "It makes estimation unnecessary"],
  "Mejora el entendimiento de lo que se construye y permite centrarse en lo que más valor aporta y más reduce los riesgos identificados.")
q("3.2.1", "Frequent stakeholder feedback throughout the SDLC can:",
  "Prevent misunderstandings about requirements and ensure changes are understood and implemented earlier",
  ["Freeze the requirements for the whole project",
   "Guarantee that no defects reach production",
   "Eliminate the need for reviews"],
  "Previene malentendidos sobre requisitos y asegura que los cambios se entienden e implementan antes.")
q("3.2.1", "A failure to deliver what the stakeholder wants can result in:",
  "Costly rework, missed deadlines and blame games",
  ["Higher test coverage",
   "Faster time to market",
   "Lower maintenance costs"],
  "El syllabus enumera retrabajo costoso, plazos incumplidos, búsqueda de culpables e incluso el fracaso completo del proyecto.")
q("3.2.1", "When should stakeholder feedback be obtained, according to the syllabus?",
  "Early and frequently throughout the SDLC",
  ["Only at the end of the project",
   "Only during acceptance testing",
   "Only when a defect is found"],
  "La sección 3.2.1 trata precisamente de los beneficios del feedback temprano y frecuente a lo largo de todo el ciclo de vida.")

# ---------------- FL-3.2.2 (K2) Review process activities ----------------
q("3.2.2", "In which activity of the review process do reviewers examine the work product and log anomalies, recommendations and questions?",
  "Individual review",
  ["Planning",
   "Review initiation",
   "Communication and analysis"],
  "Actividades: planificación, inicio de la revisión, revisión individual, comunicación y análisis, y corrección e informe. En la revisión individual cada revisor examina y registra anomalías.")
q("3.2.2", "During which review activity are the scope, purpose, quality characteristics to evaluate and exit criteria defined?",
  "Planning",
  ["Review initiation",
   "Individual review",
   "Fixing and reporting"],
  "En la planificación se define el alcance: propósito, producto a revisar, características de calidad, áreas de foco, criterios de salida, información de apoyo, esfuerzo y plazos.")
q("3.2.2", "What is the goal of review initiation?",
  "To make sure that everyone and everything involved is prepared to start the review",
  ["To decide the quality level of the reviewed work product",
   "To create defect reports for every anomaly",
   "To define the scope and exit criteria of the review"],
  "En el inicio se asegura que todos tengan acceso al producto, entiendan su rol y reciban lo necesario.")
q("3.2.2", "Why must anomalies identified during a review be analysed and discussed?",
  "Anomalies are not necessarily defects, so their status, ownership and required actions must be decided",
  ["Because every anomaly must be fixed immediately by the reviewer",
   "Because anomalies are always failures",
   "Because the author is not allowed to see them otherwise"],
  "En comunicación y análisis se decide, para cada anomalía, su estado, responsable y acciones; no todas son defectos. Suele hacerse en una reunión de revisión.")
q("3.2.2", "In which review activity are defect reports created and the work product accepted once exit criteria are reached?",
  "Fixing and reporting",
  ["Communication and analysis",
   "Individual review",
   "Review initiation"],
  "En corrección e informe se crea un informe por cada defecto para dar seguimiento y, al cumplirse los criterios de salida, el producto puede aceptarse; se informan los resultados.")
q("3.2.2", "Which standard defines the generic review process referred to in the syllabus?",
  "ISO/IEC 20246",
  ["ISO/IEC 25010",
   "ISO/IEC/IEEE 29119-4",
   "ISO 31000"],
  "La norma ISO/IEC 20246 define un proceso de revisión genérico, estructurado pero flexible, que puede adaptarse.")

# ---------------- FL-3.2.3 (K1) Roles in reviews ----------------
q("3.2.3", "Which review role ensures the effective running of review meetings, including mediation, time management and a safe review environment?",
  "Moderator (facilitator)",
  ["Scribe (recorder)",
   "Review leader",
   "Manager"],
  "El moderador asegura el buen desarrollo de las reuniones. El escriba registra anomalías y decisiones; el líder de la revisión asume la responsabilidad global; el manager decide qué revisar y da recursos.")
q("3.2.3", "Which review role decides what is to be reviewed and provides resources such as staff and time?",
  "Manager",
  ["Review leader",
   "Moderator",
   "Author"],
  "El manager decide qué se revisa y proporciona los recursos.")
q("3.2.3", "Which review role collates anomalies from reviewers and records decisions and new anomalies found during the review meeting?",
  "Scribe (recorder)",
  ["Moderator",
   "Reviewer",
   "Author"],
  "El escriba (recorder) recopila anomalías y registra información de la revisión.")
q("3.2.3", "Which review role takes overall responsibility for the review, such as deciding who will be involved and organizing when and where it will take place?",
  "Review leader",
  ["Moderator",
   "Manager",
   "Scribe"],
  "El líder de la revisión asume la responsabilidad global: decide quién participa y organiza cuándo y dónde.")
q("3.2.3", "Which review role creates and fixes the work product under review?",
  "Author",
  ["Reviewer",
   "Scribe",
   "Review leader"],
  "El autor crea y corrige el producto de trabajo revisado.")
q("3.2.3", "Who can act as a reviewer?",
  "Someone working on the project, a subject matter expert, or any other stakeholder",
  ["Only certified testers",
   "Only the author's manager",
   "Only people outside the organization"],
  "Un revisor puede ser alguien del proyecto, un experto en la materia o cualquier otro stakeholder.")

# ---------------- FL-3.2.4 (K2) Review types ----------------
q("3.2.4", "Which review type is the most formal, follows the complete generic process, collects metrics and aims to find the maximum number of anomalies?",
  "Inspection",
  ["Walkthrough",
   "Informal review",
   "Technical review"],
  "La inspección es la más formal: sigue el proceso genérico completo, recoge métricas y busca el máximo de anomalías. El autor no puede ser líder ni escriba.")
q("3.2.4", "Which review type is led by the author?",
  "Walkthrough",
  ["Inspection",
   "Technical review",
   "Informal review"],
  "El walkthrough lo dirige el autor y puede tener objetivos muy variados: evaluar calidad, formar a revisores, lograr consenso, generar ideas o detectar anomalías.")
q("3.2.4", "Which review type is performed by technically qualified reviewers, led by a moderator, with the objective of gaining consensus and making decisions regarding a technical problem?",
  "Technical review",
  ["Walkthrough",
   "Informal review",
   "Inspection"],
  "La revisión técnica la hacen revisores técnicamente cualificados, la dirige un moderador y busca consenso y decisiones sobre un problema técnico, además de detectar anomalías.")
q("3.2.4", "Which statement about informal reviews is correct?",
  "They do not follow a defined process and do not require a formal documented output",
  ["They always collect metrics",
   "The author cannot participate",
   "They require a trained moderator"],
  "Las revisiones informales no siguen un proceso definido ni requieren salida documentada formal. Su objetivo principal es detectar anomalías.")
q("3.2.4", "In which review type can the author NOT act as the review leader or scribe?",
  "Inspection",
  ["Walkthrough",
   "Informal review",
   "Technical review"],
  "En las inspecciones el autor no puede actuar como líder de la revisión ni como escriba.")
q("3.2.4", "Which factor influences the required level of formality of a review?",
  "Legal or regulatory requirements and the need for an audit trail",
  ["The number of pages printed",
   "The favourite review type of the author",
   "The time zone of the reviewers"],
  "La formalidad depende del ciclo de vida, la madurez del proceso, la criticidad y complejidad del producto, los requisitos legales o regulatorios y la necesidad de pista de auditoría.")
q("3.2.4", "Which statement about review types is correct?",
  "The same work product can be reviewed with different review types, e.g., first informally and later more formally",
  ["Each work product may only be reviewed once",
   "Walkthroughs always require individual preparation",
   "Inspections do not use metrics"],
  "El syllabus indica que un mismo producto puede revisarse con distintos tipos, primero uno informal y después uno más formal.")

# ---------------- FL-3.2.5 (K1) Success factors for reviews ----------------
q("3.2.5", "Which of the following is a success factor for reviews?",
  "Performing reviews on small chunks so that reviewers do not lose concentration",
  ["Using review results to evaluate the performance of the author",
   "Reviewing as much material as possible in a single session",
   "Skipping reviewer training to save time"],
  "Factores de éxito: objetivos claros y criterios de salida medibles, tipo de revisión adecuado, trozos pequeños, feedback, tiempo para preparar, apoyo de la dirección, cultura, formación y facilitación de reuniones.")
q("3.2.5", "According to the syllabus, what should NEVER be an objective of a review?",
  "Evaluation of the participants",
  ["Detecting anomalies",
   "Building confidence in the work product",
   "Gaining consensus"],
  "El syllabus es explícito: la evaluación de los participantes nunca debe ser un objetivo.")
q("3.2.5", "Which of the following is a success factor for reviews?",
  "Support from management for the review process",
  ["Keeping review results secret from authors",
   "Avoiding any preparation time",
   "Choosing the most formal review type for every work product"],
  "El apoyo de la dirección es un factor de éxito. Además hay que elegir el tipo de revisión adecuado al objetivo y al contexto, no siempre el más formal.")
q("3.2.5", "Which success factor helps authors and stakeholders improve the product and their activities?",
  "Providing feedback from reviews to stakeholders and authors",
  ["Excluding authors from the review meeting",
   "Holding reviews without any agenda",
   "Limiting reviews to the test team"],
  "Proporcionar feedback de las revisiones a stakeholders y autores les permite mejorar el producto y sus actividades.")
q("3.2.5", "Which of the following is a success factor for reviews?",
  "Making reviews part of the organization's culture, to promote learning and process improvement",
  ["Making reviews optional and unannounced",
   "Using reviews only when a project is late",
   "Rewarding reviewers per defect found"],
  "Integrar las revisiones en la cultura de la organización promueve el aprendizaje y la mejora de procesos.")
q("3.2.5", "Which of the following is a success factor for reviews?",
  "Providing adequate training for all participants so they know how to fulfil their role",
  ["Allowing only the author to define the exit criteria after the review",
   "Avoiding measurable exit criteria",
   "Starting the review meeting without individual preparation"],
  "La formación adecuada de todos los participantes es un factor de éxito, igual que definir objetivos claros y criterios de salida medibles.")
