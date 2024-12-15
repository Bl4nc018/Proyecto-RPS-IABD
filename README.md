# Piedra, Papel, Tijera (RPS)

---

## Índice

1. [Especificación del entorno de tareas](#1-especificación-del-entorno-de-tareas)  
2. [Identificación del tipo de agente y estructura](#2-identificación-del-tipo-de-agente-y-estructura)  
3. [Implementación en Python](#3-implementación-en-python)  
4. [Extensión al RPS + Lagarto y Spock](#4-extensión-al-rps-+-lagarto-y-spock)  

---

## 1. Especificación del entorno de tareas

O xogo de **Pedra, Papel, Tesoura (RPS)** pode analizarse segundo as propiedades descritas na sección _"2.3.2 Properties of Task Environments"_ do libro _Artificial Intelligence: A Modern Approach_ de Russell e Norvig. A táboa seguinte resume as características do contorno:

Primero, se analizarán las propiedades del entorno para poder escoger el agente adecuado. En la siguiente tabla se resumen las características del entorno:

| **Propiedad**        | **Descripción breve**                                                                                    |
|-----------------------|---------------------------------------------------------------------------------------------------------|
| **Observable**        | **Completamente observable**:El agente conoce toda la información relevante del entorno en cada ronda.  |
| **Agentes**           | **Multi-agente**: El juego involucra dos jugadores (máquina y humano, o dos máquinas)                   |
| **Adversarial**       | **Adversarial**: El éxito de un jugador depende directamente del fallo del otro                         |
| **Determinista**      | **Determinista**: Las acciones de ambos jugadores determinan el resultado de la ronda sin incerteza.    |
| **Secuencial**        | **Secuencial**: El agente depende del historial acumulado, el que conecta las decisiones entre rondas.  |
| **Estático**          | **Estático**: El estado del entorno no cambia mientras el agente no toma decisiones.                    |
| **Discreto**          | **Discreto**: Las acciones y estados posibles son finitos y bien definidos (piedra, papel, tijera)      |
| **Conocido**          | **Conocido**: Las reglas y resultados del juego son completamente comprensibles y especificados.        |


### Justificación de las propiedades 

1. **Observable**:El entorno es totalmente observable porque el agente tiene acceso a toda la información relevante en cada momento, como la última acción del oponente y las reglas del juego. La incertidumbre sobre la próxima acción no implica falta de información observable, sino la naturaleza competitiva del juego.

2. **Agentes**: El juego es claramente un entorno multi-agente, ya que las decisiones de cada jugador afectan directamente al resultado final. La interacción es competitiva, dado que el éxito de un jugador implica el fallo de otro.

3. **Adversarial**: El juego es adversarial porque los objetivos de los dos agentes están en conflicto: el éxito de uno es el fallo del otro. Esto hace que el agente deba analizar estrategias que maximizan su probabilidad de éxito.

4. **Determinista**: El juego es determinista, dado que la combinación de acciones (piedra, papel, tijera) tiene un resultado fijo predefinido. No hay elementos de aleatoriedad inherente en las reglas del juego.

5. **Secuencial**: El entorno es secuencial porque las decisiones del agente están influídas por el historial acumulado de las rondas previas. El modelo interno emplea estas observaciones para predecir futuras acciones del oponente y mejorar el rendimiento del agente.

6. **Estático**: El entorno es estático porque no cambia mientras el agente toma su decisión. No hay eventos externos ni variaciones en el estado de juego durante la deliberación.

7. **Discreto**: El juego es discreto, ya que las acciones posibles son finitas (piedra, papel, tijera) y están perfectamente definidas. No hay estados continuos ni transiciones indefinidas.

8. **Conocido**: El entorno es conocido, ya que las reglas del juego están completamente especificadas y el agente no necesita aprender las interacciones entre acciones.

---

