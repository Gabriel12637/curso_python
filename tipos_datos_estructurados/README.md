La construcción anterior sólo define un nuevo tipo de datos, no se declara variable alguna. Es decir, la construcción anterior tiene la misma entidad que el tipo “int” o “float”. El nombre del nuevo tipo estructurado definido es “struct nombre_de_la_estructura”. Por ejemplo:
#define FIRST_SIZE 100
#define LAST_SIZE 200
#define CONTACTS_NUM 100

/* Definición de la estructura */
struct contact_information 
{
    char firstname[FIRST_SIZE];
    char lastname[LAST_SIZE];
    unsigned int homephone;
    unsigned int mobilephone;
};

/* Declaración de variables con esta estructura */
struct contact_information person1, person2, contacts[CONTACTS_NUM]
as líneas 6 a 12 definen un nuevo tipo de datos estructurado que contiene cuatro campos, los dos primeros son tablas de letras y los dos últimos son enteros. A pesar de que estos campos tienen nombres y tamaños, hasta el momento no se ha declarado ninguna variable. Es en la línea 15 en la que se sí se declaran tres variables de este nuevo tipo estructurado. La última de ellas es una tabla de 100 de estas estructuras. Asegúrate de que tienes clara la diferencia entre la “definición” de un tipo de datos y la “declaración” de variables de ese tipo. La siguiente figura muestra estos conceptos para una estructura y un tipo básico.

struct contact_information 
{
    char firstname[FIRST_SIZE];
    char lastname[LAST_SIZE];
    unsigned int homephone;
    unsigned int mobilephone;
} person1, person2 contacts[CONTACTS_NUM]