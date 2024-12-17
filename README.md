# Piedra, Papel, Tijera (RPS)

En este proyecto se aplicarán principios de **Inteligencia Artificial** para crear una versión del juego **Piedra, Papel y Tijera**. Se programará un agente inteligente que busca poner una solución al entorno de tareas del juego mencionado en función a las directrices mostradas en el capítulo 2 del libro: _Intelligent Agents do libro IA: A modern approach, Russell & Norvig_.

## Índice

1. [Especificación del entorno de tareas](#1-especificación-del-entorno-de-tareas)  
2. [Identificación del tipo de agente y estructura](#2-identificación-del-tipo-de-agente-y-estructura)  
3. [Implementación en Python](#3-implementación-en-python)  
4. [Extensión al RPS + Lagarto y Spock](#4-extensión-al-rps-+-lagarto-y-spock)  

---

## 1. Especificación del entorno de tareas

Primero, se analizarán las propiedades del entorno para poder escoger el agente adecuado. En la siguiente tabla se resumen las características del entorno:

| **Propiedad**         | **Descripción breve**                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| **Observable**        | **Parcialmente observable**: El agente no conoce la acción del oponente hasta después de decidir la suya.  |
| **Agentes**           | **Multi-agente**: El juego involucra dos jugadores (máquina y/o humano)                                    |
| **Determinista**      | **Determinista**: Las acciones de ambos jugadores determinan el resultado de la ronda sin incerteza.       |
| **Secuencial**        | **Secuencial**: El agente depende del historial acumulado, el que conecta las decisiones entre rondas.     |
| **Estático**          | **Estático**: El estado del entorno no cambia mientras el agente no toma decisiones.                       |
| **Discreto**          | **Discreto**: Las acciones y estados posibles son finitos y bien definidos (piedra, papel, tijera)         |
| **Conocido**          | **Conocido**: Las reglas y resultados del juego son completamente comprensibles y especificados.           |

### Justificación de las propiedades 

1. **Observable**: El entorno es parcialmente observable porque el agente, pese a conocer las reglas del juego y las acciones posibles, le es imposible saber cual será la acción del oponente en el momento de tomar su decisión, dado que ambos actuan simultáneamente. 

2. **Agentes**: El juego es un entorno multi-agente adversarial, ya que participan dos agentes (jugadores o máquinas) cuyas decisiones afectan directamente al resultado final. La interacción es competitiva, dado que el éxito de un jugador implica el fallo del otro.

3. **Determinista**: El juego es determinista, dado que la combinación de acciones (piedra, papel, tijera) tiene un resultado fijo predefinido. No hay elementos de aleatoriedad inherente en las reglas del juego.

4. **Secuencial**: El entorno es secuencial porque las decisiones del agente están influídas por el historial acumulado de las rondas previas. El modelo interno emplea estas observaciones para predecir futuras acciones del oponente y mejorar el rendimiento del agente.

5. **Estático**: El entorno es estático porque no cambia mientras el agente toma su decisión. No hay eventos externos ni variaciones en el estado de juego durante la deliberación.

6. **Discreto**: El juego es discreto, ya que las acciones posibles son finitas (piedra, papel, tijera) y están perfectamente definidas. No hay estados continuos ni transiciones indefinidas.

7. **Conocido**: El entorno es conocido, ya que las reglas del juego están completamente especificadas y el agente no necesita aprender las interacciones entre acciones.

---