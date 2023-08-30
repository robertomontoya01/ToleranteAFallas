#include <iostream>
#include <stdexcept>

double divide(double a, double b) {
    if (b == 0) {
        throw std::runtime_error("División por cero");
    }
    return a / b;
}

int main() {
    try {
        double result = divide(10.0, 0.0);
        std::cout << "Resultado: " << result << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}

/*

En este ejemplo, la función divide verifica si el divisor b es cero y, si lo es, lanza una excepción de tipo std::runtime_error. 
En el bloque try en la función main, se llama a divide con argumentos y se captura cualquier excepción que se arroje en el bloque catch. 
Si se lanza la excepción, se imprime un mensaje de error.

*/
