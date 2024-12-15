## Estructura do proxecto / rubrica

A documentación presentada no `README.md` debe **seguir esta orde e título de epígrafes:**

1.**Especificación do contorna de tarefas**

Especifica todas as características da contorna de tarefas do RPS, justificando cada unha con precisión segundo a sección _"2.3.2 Properties of task environments"_ do libro _"IA: A Modern Approach"_ de Russell & Norvig.

2.**Identificación do tipo de axente e estrutura**

Selecciona un tipo de axente adecuado para o RPS e debuxa un modelo preciso da estrutura do axente, incluíndo os compoñentes específicos do tipo elixido, baseándoche nos conceptos do capítulo 2 _"Intelligent Agents"_.

É moi importante que ademáis da figura escribas un texto enumerando e xustificando a presenza dous comppñentes recollidos na figura anterior. Sen explicacións a figura non se avalía.

3.**Implementación en Python**

Implementa en Python todos os compoñentes da estrutura do axente de forma correcta e eficiente, creando unha función axente que xoga ao RPS seguindo a lóxica do tipo de axente seleccionado. O código cumpre cos principios SOLID, especialmente SRP e OCP, permitindo estender a lóxica a outras versións do xogo. **A estratexia implementada en `get_computer_action()` é creativa e busca maximizar o rendemento do axente**.

O teu código pode e debe ser modular seguindo o principio SRP, pero **a execución da lóxica ten que invocarse dende a función `get_computer_action()`.

A rúbrica da implementación Python [na segunda folla "RPS" deste libro de cálculo.](https://docs.google.com/spreadsheets/d/1r93uZnPmioY0U1D7EDtV1uveKYIOlenkz8uuqks4KXM/) Loguéate antes na túa conta de gmail con acceso ao noso Drive.

4.**Extensión ao RPS + Lizzard Spock**

- Estende a lóxica do axente para xogar á versión "pedra, papel, tesoiras, lagarto, Spock" correctamente, mantendo a calidade do código e a coherencia co tipo de axente seleccionado. 

- A documentación no README do proxecto en GitHub/GitLab deber estar completa seguindo a orde especificada nesta rúbrica, explicando o problema, a contorna de tarefas, a estrutura do axente, a implementación e a extensión, cun formato Markdown axeitado.
