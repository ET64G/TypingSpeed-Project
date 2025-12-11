"""
Text Generator Module
Provides sample text passages for typing tests with different difficulty levels.
"""

import random


class TextGenerator:
    """Generates sample text for typing tests"""
    
    # Easy texts (short, common words)
    EASY_TEXTS = [
        "The quick brown fox jumps over the lazy dog. This is a simple sentence for practice.",
        "I love to code and build applications. Programming is fun and creative.",
        "The sun shines bright in the sky. Birds fly high above the clouds.",
        "Reading books helps you learn new things. Knowledge is power and wisdom.",
        "Friends are important in life. They help you when you need support.",
        "Music makes people happy. Songs can change your mood instantly.",
        "Food is essential for survival. We need to eat healthy meals every day.",
        "Exercise keeps your body strong. Running and walking are good activities.",
        "Learning new skills takes time. Practice makes perfect in everything.",
        "Nature is beautiful and peaceful. Trees and flowers make the world colorful."
    ]
    
    # Medium texts (longer sentences, varied vocabulary)
    MEDIUM_TEXTS = [
        "The development of technology has transformed how we communicate and work in modern society. "
        "Computers and smartphones have become essential tools for daily life, enabling us to connect "
        "with people around the world instantly.",
        
        "Education plays a crucial role in personal growth and career advancement. Students who "
        "dedicate time to learning new concepts and practicing skills tend to achieve better results "
        "in their academic and professional pursuits.",
        
        "Climate change represents one of the most significant challenges facing humanity today. "
        "Scientists and researchers are working diligently to develop solutions that can help reduce "
        "carbon emissions and protect our planet for future generations.",
        
        "The art of storytelling has been practiced for thousands of years across different cultures. "
        "Stories help us understand complex ideas, share experiences, and connect with others on "
        "an emotional level that transcends language barriers.",
        
        "Innovation drives progress in every field, from medicine to engineering to the arts. "
        "Creative thinking and problem-solving skills are essential for developing new technologies "
        "and solutions that improve quality of life for people everywhere.",
        
        "Travel broadens the mind and exposes us to new perspectives and ways of living. "
        "Experiencing different cultures helps build empathy and understanding between people "
        "from diverse backgrounds and traditions.",
        
        "The importance of maintaining good health cannot be overstated. Regular exercise, "
        "balanced nutrition, and adequate sleep form the foundation of a healthy lifestyle "
        "that supports both physical and mental well-being.",
        
        "Reading literature enhances vocabulary, improves comprehension skills, and stimulates "
        "imagination. Books offer windows into different worlds and perspectives that expand "
        "our understanding of human nature and society.",
        
        "Teamwork and collaboration are essential skills in both professional and personal settings. "
        "Working effectively with others requires communication, compromise, and a shared commitment "
        "to achieving common goals and objectives.",
        
        "The digital age has revolutionized how we access information and entertainment. "
        "The internet provides instant access to vast amounts of knowledge, connecting learners "
        "and educators across the globe in unprecedented ways."
    ]
    
    # Hard texts (complex vocabulary, technical terms, longer passages)
    HARD_TEXTS = [
        "The intricate mechanisms underlying quantum computing represent a paradigm shift in "
        "computational methodology. Quantum bits, or qubits, exploit superposition and entanglement "
        "principles to process information exponentially faster than classical computers, potentially "
        "revolutionizing cryptography, drug discovery, and artificial intelligence applications.",
        
        "Philosophical inquiry into the nature of consciousness and free will continues to challenge "
        "our fundamental assumptions about human experience. The hard problem of consciousness, "
        "articulated by philosophers like David Chalmers, questions whether subjective experience "
        "can be fully explained through physical processes alone, raising profound implications "
        "for our understanding of mind and reality.",
        
        "The synthesis of organic compounds through sophisticated chemical reactions requires "
        "meticulous attention to reaction conditions, stoichiometry, and mechanistic pathways. "
        "Modern organic chemistry employs advanced spectroscopic techniques and computational "
        "modeling to predict and verify molecular structures, enabling the development of "
        "pharmaceuticals and materials with precise properties.",
        
        "Economic theories regarding market efficiency and behavioral finance reveal the complex "
        "interplay between rational decision-making and psychological biases. The efficient market "
        "hypothesis suggests that asset prices reflect all available information, while behavioral "
        "economists demonstrate how cognitive limitations and emotional factors influence investment "
        "decisions in ways that deviate from purely rational models.",
        
        "The architectural principles underlying distributed systems design emphasize scalability, "
        "fault tolerance, and consistency guarantees. Microservices architectures decompose monolithic "
        "applications into independently deployable components, enabling teams to develop and "
        "maintain complex software systems with greater agility and resilience.",
        
        "Literary analysis of postmodern narratives reveals how authors deconstruct traditional "
        "storytelling conventions to challenge readers' expectations and explore themes of identity, "
        "reality, and meaning. Metafictional techniques blur boundaries between fiction and reality, "
        "inviting readers to question the nature of narrative truth and authorial authority.",
        
        "The molecular biology of gene expression involves intricate regulatory networks that "
        "coordinate transcription, translation, and post-translational modifications. Epigenetic "
        "mechanisms, including DNA methylation and histone modifications, modulate gene activity "
        "without altering the underlying genetic sequence, providing a layer of complexity to "
        "our understanding of heredity and development.",
        
        "Theoretical frameworks in cognitive psychology explore how humans acquire, process, "
        "and retrieve information through complex neural networks. Working memory models propose "
        "multi-component systems that temporarily store and manipulate information, while long-term "
        "memory research distinguishes between declarative and procedural knowledge systems.",
        
        "The mathematical foundations of machine learning algorithms rely on optimization theory, "
        "linear algebra, and statistical inference. Gradient descent methods iteratively adjust "
        "model parameters to minimize loss functions, while regularization techniques prevent "
        "overfitting and improve generalization to unseen data.",
        
        "The historical evolution of democratic institutions reveals ongoing tensions between "
        "majority rule and minority rights, individual liberty and collective security. "
        "Constitutional frameworks attempt to balance these competing values through separation "
        "of powers, checks and balances, and enumerated rights that limit governmental authority."
    ]
    
    @classmethod
    def get_text(cls, difficulty="medium", random_selection=True):
        """
        Get a sample text for typing test
        
        Args:
            difficulty: "easy", "medium", or "hard"
            random_selection: If True, return random text; if False, return first text
        
        Returns:
            str: Sample text for typing practice
        """
        if difficulty.lower() == "easy":
            texts = cls.EASY_TEXTS
        elif difficulty.lower() == "hard":
            texts = cls.HARD_TEXTS
        else:  # medium (default)
            texts = cls.MEDIUM_TEXTS
        
        if random_selection:
            return random.choice(texts)
        else:
            return texts[0]
    
    @classmethod
    def get_random_text(cls):
        """Get a random text from any difficulty level"""
        all_texts = cls.EASY_TEXTS + cls.MEDIUM_TEXTS + cls.HARD_TEXTS
        return random.choice(all_texts)
    
    @classmethod
    def get_text_by_length(cls, min_length=100, max_length=500):
        """
        Get a text within specified length range
        
        Args:
            min_length: Minimum character length
            max_length: Maximum character length
        
        Returns:
            str: Text within specified length range
        """
        all_texts = cls.EASY_TEXTS + cls.MEDIUM_TEXTS + cls.HARD_TEXTS
        
        # Filter texts by length
        suitable_texts = [text for text in all_texts 
                         if min_length <= len(text) <= max_length]
        
        if suitable_texts:
            return random.choice(suitable_texts)
        else:
            # If no text matches, return closest match
            return min(all_texts, key=lambda x: abs(len(x) - (min_length + max_length) / 2))

