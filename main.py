import multiprocessing
import time

def incrementar_contador(contador, lock, proceso_id):
    for _ in range(10):
        with lock:
            contador.value += 1
        print(f"Proceso {proceso_id}: Incremento en 1, Contador actual: {contador.value}")
        time.sleep(1)

if __name__ == "__main__":
    # Crear un contador compartido y un lock
    contador = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    # Crear dos procesos
    proceso1 = multiprocessing.Process(target=incrementar_contador, args=(contador, lock, 1))
    proceso2 = multiprocessing.Process(target=incrementar_contador, args=(contador, lock, 2))

    # Iniciar los procesos
    proceso1.start()
    proceso2.start()

    # Esperar a que ambos procesos terminenn
    proceso1.join()
    proceso2.join()

    print("Contador final:", contador.value)
