unidades = {
    1: "I",
    5: "V",
    10:"X",
}

decenas = {
   1: "X",
   5: "L",
   10: "C"
}

centenas = {
   1: "C",
   5: "D",
   10: "M"
}

millares = {
   1: "M"
}

class RomanNumberError(Exception):
   pass

def listar_numero(num):
   n_mil = num // 1000 * 1000
   n_cen = (num % 1000) // 100 * 100
   n_dec = (num % 100)//10*10
   n_uni = (num % 10)

   return n_mil,n_cen,n_dec,n_uni

def sacar_clave(num): #3546
   if num >= 1000:    
      clave = millares
      num = num // 1000
   elif num >= 100:
      clave = centenas
      #num //=100   
      num = num//100
   elif num >= 10:
      clave = decenas
      num = num // 10
   else:
         clave = unidades
   return clave,num

def logica_aplastante(digito,clau):
   res = ""
   if digito < 4:                            
      res += digito * clau[1]       
   elif digito == 4:   
      res += clau[1] + clau [5]                      
   elif digito< 9:
      num_palitos = digito -5
      res += clau[5] + num_palitos * clau[1]
   else:
      res += clau[1] + clau[10]
   return res
def entero_a_romano(n_int):
   

   if n_int > 3999:
      raise RomanNumberError("El número debe ser inferior a 4000")

   digitos = listar_numero(n_int)  #3000,500,50,6
   
   resultado = ""

   for digito in digitos:
      if digito == 0:
         continue
      
      clave, digito = sacar_clave(digito)

      resultado += logica_aplastante(digito,clave) 
            
   return resultado
  
numeros_romanos = {
   "I": 1,
   "V": 5,
   "X": 10,
   "L": 50,
   "C": 100,
   "D": 500,
   "M": 1000
}

def comprueba_excepciones(romano):
   for simbolo in numeros_romanos:
      if simbolo * 4 in romano:
         raise RomanNumberError("No se admiten más de tres simbolos iguales") 
      elif simbolo in "VLD" and simbolo *2 in romano:
         raise RomanNumberError("No admite mas de dos veces V, L O D")
      


def romano_a_entero(letras):
   valor_total = 0
   ultimo_valor = 0
   valor_final = 0

   comprueba_excepciones(letras)

   for numeral in reversed(letras):  #3546 -- MMMDXXLVI - IVLXDMMM
      valor_actual = numeros_romanos[numeral]

      if valor_actual <= 5 and ultimo_valor >= 50:
         raise RomanNumberError ("Resta no permitida")
      if valor_actual <= 50 and ultimo_valor >= 500:
         raise RomanNumberError ("Resta no permitida")
      

      if valor_actual < valor_final:
         raise RomanNumberError("No esta ordenado ascendente")
      elif valor_final == valor_actual and ultimo_valor > valor_actual:
         raise RomanNumberError("Otras dos restas seguidas")

      if valor_actual >= ultimo_valor:
         valor_total += valor_actual   
      elif numeral not in "VLD":
         valor_total -= valor_actual
      else:
         raise RomanNumberError("Resta de multiplo 5 no permitida")
      
      valor_final = ultimo_valor
      ultimo_valor = valor_actual
   return valor_total

   


if __name__=="__main__":
   print(entero_a_romano)
