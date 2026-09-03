# Password Security Analyser

A terminal-based educational tool for analysing password security and demonstrating fundamental cybersecurity concepts.

The project will analyse password characteristics such as length and character variety, calculate estimated entropy using:

$$
H = L\log_2(N)
$$

and provide an educational assessment of password strength.

As the project develops, it will explore additional concepts including password predictability, brute-force attacks, secure password generation, cryptographic hashing, and multi-factor authentication (MFA).

## Current Status

**Early development**

The project is currently being set up. Initial functionality will focus on basic password analysis and theoretical entropy calculation.

## Planned Features

* Password length analysis
* Character variety analysis
* Estimated entropy calculation
* Basic password strength assessment
* Pattern and predictability detection
* Common password detection
* Brute-force attack modelling
* Secure password generation
* Password hashing and salting demonstrations
* Authentication and MFA concepts

## Technologies

* Python
* Terminal / CLI

## Educational Purpose

This project is primarily intended as a learning exercise. It aims to explore how password security works from both a defensive and attacker-perspective.

The entropy calculation represents a theoretical estimate based on the assumed character set and password length. Human-created passwords are often predictable and may therefore have significantly less effective security than their theoretical entropy suggests.

The project will explore this distinction as additional password analysis features are introduced.

## Future Development

The project will be developed incrementally, with each phase introducing new cybersecurity concepts and functionality.
