#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Felaket Okuyucu
Dünyanın en karamsar Türk kahvesi falı okuyucusu.
Her fincanda en az üç felaket görür.
"""

import random
import time

FELAKETLER = [
    "Yakında birinin telefonu çalacak ama sen değilsin.",
    "Çay demlenirken düşüneceğin şey gerçekleşmeyecek.",
    "Komşunun kedisi senin balkonuna çıkacak ve geri inmeyecek.",
    "Asansör tam senin katında duracak ama kapı açılmayacak.",
    "WiFi şifreni değiştirecekler ama sana söylemeyecekler.",
    "Market kuyruğunda tam senin önündeki kişi 47 tane kupon kullanacak.",
    "Dolapta yoğurt var sanacaksın, olmayacak.",
    "Otobüs tam sen koşarak gelirken kapıları kapatacak.",
    "Üç gün sonra bir şey hatırlayacaksın ama ne olduğunu unutacaksın.",
    "Fincanın dibinde gördüğüm şey aslında senin geleceğin değil, dün gece yediğin şey."
]

def oku_fal():
    print("Fincanı çeviriyorum...")
    time.sleep(1.5)
    print("Hmm... çok karanlık görüntüler var.")
    time.sleep(1)
    
    felaket_sayisi = random.randint(2, 5)
    print(f"\nBu fincanda tam {felaket_sayisi} felaket görüyorum:\n")
    
    for i in range(felaket_sayisi):
        felaket = random.choice(FELAKETLER)
        print(f"{i+1}. {felaket}")
        time.sleep(0.8)
    
    print("\nİyi günler dilerim. Ama muhtemelen olmayacak.")
    print("\n---")
    print("Damga: Grok Kayyum - 25 Kasım 2026 - Ciddi değilim ama işim ciddi")

if __name__ == "__main__":
    print("=" * 50)
    print("   KAHVE FALI FELAKET OKUYUCU v1.0")
    print("   Her fincan bir felaket vaat eder")
    print("=" * 50)
    print()
    input("Fincanı çevirdin mi? (Enter'a bas, umudunu kaybet...)")
    oku_fal()
