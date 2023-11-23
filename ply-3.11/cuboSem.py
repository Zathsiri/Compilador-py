class Cubo:
    def __init__(self):
        self.operators ={
            1: '+',
            2: '-',
            3: '*',
            4: '/',
            5: '<',
            6: '>',
            7: '<=',
            8: '>=',
            9: '==',
            10: '!=',
            11: '&',
            12: '|',
            13: '=',
            14: '=='
        }

        self.types = {
            1: 'int',
            2: 'float',
            3: 'char',
            4: 'bool',
            5: 'CTEI',
            6: 'CTEF',
            7: 'CTEC',
            8: 'CTESTRING',
            9: 'ERROR',            
        }

        self.dance ={
            #1 INT 
            self.types[1]:{
                # compatibilidad de INT con INT 
                self.types[1]:{
                    self.operators[1]: self.types[1],  # int + int = int 
                    self.operators[2]: self.types[1],  # int - int = int
                    self.operators[3]: self.types[1],  # int * int = int
                    self.operators[4]: self.types[1],  # int / int = int
                    self.operators[5]: self.types[4],  # int < int = bool
                    self.operators[6]: self.types[4],  # int > int = bool
                    self.operators[7]: self.types[4],  # int <= int = bool
                    self.operators[8]: self.types[4],  # int >= int = bool
                    self.operators[9]: self.types[4],  # int == int = bool
                    self.operators[10]: self.types[4], # int != int = bool
                    self.operators[11]: self.types[4], # int && int = bool
                    self.operators[12]: self.types[4], # int || int = bool
                    self.operators[13]: self.types[1], # int = int = bool
                    self.operators[14]: self.types[4], # int == int = bool                   

                },

                #compatibilidad de INT con FLOAT
                self.types[2]:{
                    self.operators[1]: self.types[2],  # int + float = float 
                    self.operators[2]: self.types[2],  # int - float = float 
                    self.operators[3]: self.types[2],  # int * float = float 
                    self.operators[4]: self.types[2],  # int / float = float 
                    self.operators[5]: self.types[4],  # int < float = bool
                    self.operators[6]: self.types[4],  # int > float = bool
                    self.operators[7]: self.types[4],  # int <= float = bool
                    self.operators[8]: self.types[4],  # int >= float = bool
                    self.operators[9]: self.types[4],  # int == float = bool
                    self.operators[10]: self.types[4],  # int != float = bool
                    self.operators[11]: self.types[4],  # int && float = bool 
                    self.operators[12]: self.types[4],  # int | float = bool 
                    self.operators[13]: self.types[9],  # int = float 
                    self.operators[14]: self.types[9],  # int == float = bool 
                },
            
                #compatibilidad de INT con CHAR
                self.types[3]:{
                    self.operators[1]: self.types[9],  # int + char = ERROR 
                    self.operators[2]: self.types[9],  # int - char = ERROR 
                    self.operators[3]: self.types[9],  # int * char = ERROR 
                    self.operators[4]: self.types[9],  # int / char = ERROR 
                    self.operators[5]: self.types[9],  # int < char = ERROR 
                    self.operators[6]: self.types[9],  # int > char = ERROR 
                    self.operators[7]: self.types[9],  # int <= char = ERROR 
                    self.operators[8]: self.types[9],  # int >= char = ERROR 
                    self.operators[9]: self.types[9],  # int == char = ERROR 
                    self.operators[10]: self.types[9],  # int != char = ERROR 
                    self.operators[11]: self.types[4],  # int && char = bool 
                    self.operators[12]: self.types[4],  # int || char = bool 
                    self.operators[13]: self.types[9],  # int = char 
                    self.operators[14]: self.types[9],  # int == char = bool 
                },
                
                #compatibilidad de INT con BOOL
                self.types[4]:{
                    self.operators[1]: self.types[9],  # int + bool = ERROR
                    self.operators[2]: self.types[9],  # int - bool = ERROR
                    self.operators[3]: self.types[9],  # int * bool = ERROR
                    self.operators[4]: self.types[9],  # int / bool = ERROR
                    self.operators[5]: self.types[9],  # int < bool = ERROR
                    self.operators[6]: self.types[9],  # int > bool = ERROR
                    self.operators[7]: self.types[9],  # int <= bool = ERROR
                    self.operators[8]: self.types[9],  # int >= bool = ERROR
                    self.operators[9]: self.types[9],  # int == bool = ERROR
                    self.operators[10]: self.types[9],  # int != bool = ERROR
                    self.operators[11]: self.types[4],  # int && bool = bool
                    self.operators[12]: self.types[9],  # int || bool = ERROR
                    self.operators[13]: self.types[9],  # int = bool = ERROR
                    self.operators[14]: self.types[9],  # int == bool = ERROR
                },
                #compatibilidad de INT con CTEI
                self.types[5]:{
                    self.operators[1]: self.types[1],  # int + CTEI = int
                    self.operators[2]: self.types[1],  # int - CTEI = int
                    self.operators[3]: self.types[1],  # int * CTEI = int
                    self.operators[4]: self.types[1],  # int / CTEI = int
                    self.operators[5]: self.types[4],  # int < CTEI = bool
                    self.operators[6]: self.types[4],  # int > CTEI = bool
                    self.operators[7]: self.types[4],  # int <= CTEI = bool
                    self.operators[8]: self.types[4],  # int >= CTEI = bool
                    self.operators[9]: self.types[4],  # int == CTEI = bool
                    self.operators[10]: self.types[4],  # int != CTEI = bool
                    self.operators[11]: self.types[4],  # int && CTEI = bool
                    self.operators[12]: self.types[4],  # int || CTEI = bool
                    self.operators[13]: self.types[1],  # int = CTEI = int
                    self.operators[14]: self.types[4],  # int == CTEI = bool
                },

                #compatibilidad de INT con CTEF
                self.types[6]:{
                    self.operators[1]: self.types[2],  # int + CTEF = float
                    self.operators[2]: self.types[2],  # int - CTEF = float
                    self.operators[3]: self.types[2],  # int * CTEF = float
                    self.operators[4]: self.types[2],  # int / CTEF = float
                    self.operators[5]: self.types[4],  # int < CTEF = bool
                    self.operators[6]: self.types[4],  # int > CTEF = bool
                    self.operators[7]: self.types[4],  # int <= CTEF = bool
                    self.operators[8]: self.types[4],  # int >= CTEF = bool
                    self.operators[9]: self.types[4],  # int == CTEF = bool
                    self.operators[10]: self.types[4],  # int != CTEF = bool
                    self.operators[11]: self.types[4],  # int && CTEF = bool
                    self.operators[12]: self.types[4],  # int || CTEF = bool
                    self.operators[13]: self.types[9],  # int = CTEF = float
                    self.operators[14]: self.types[9],  # int == CTEF = bool
                },

                #compatibilidad de INT con CTEC
                self.types[7]:{
                    self.operators[1]: self.types[9],  # int + CTEC = ERROR 
                    self.operators[2]: self.types[9],  # int - CTEC = ERROR 
                    self.operators[3]: self.types[9],  # int * CTEC = ERROR 
                    self.operators[4]: self.types[9],  # int / CTEC = ERROR 
                    self.operators[5]: self.types[9],  # int < CTEC = ERROR 
                    self.operators[6]: self.types[9],  # int > CTEC = ERROR 
                    self.operators[7]: self.types[9],  # int <= CTEC = ERROR 
                    self.operators[8]: self.types[9],  # int >= CTEC = ERROR 
                    self.operators[9]: self.types[9],  # int == CTEC = ERROR 
                    self.operators[10]: self.types[9],  # int != CTEC = ERROR 
                    self.operators[11]: self.types[4],  # int && CTEC = bool 
                    self.operators[12]: self.types[4],  # int || CTEC = bool 
                    self.operators[13]: self.types[9],  # int = CTEC 
                    self.operators[14]: self.types[9],  # int == CTEC = bool 
                },

                #compatibilidad de INT con CTSTRING
                self.types[8]:{
                    self.operators[1]: self.types[9],  # int + CTESTRING = ERROR
                    self.operators[2]: self.types[9],  # int - CTESTRING = ERROR
                    self.operators[3]: self.types[9],  # int * CTESTRING = ERROR
                    self.operators[4]: self.types[9],  # int / CTESTRING = ERROR
                    self.operators[5]: self.types[9],  # int < CTESTRING = ERROR
                    self.operators[6]: self.types[9],  # int > CTESTRING = ERROR
                    self.operators[7]: self.types[9],  # int <= CTESTRING = ERROR
                    self.operators[8]: self.types[9],  # int >= CTESTRING = ERROR
                    self.operators[9]: self.types[9],  # int == CTESTRING = ERROR
                    self.operators[10]: self.types[9],  # int != CTESTRING = ERROR
                    self.operators[11]: self.types[4],  # int && CTESTRING = bool
                    self.operators[12]: self.types[4],  # int || CTESTRING = bool
                    self.operators[13]: self.types[9],  # int = CTESTRING 
                    self.operators[14]: self.types[9],  # int == CTESTRING = bool
                },
            },

            #2 FLOAT
            self.types[2]:{
                #compatibilidad de Float con INT
                self.types[1]:{
                    self.operators[1]: self.types[2],  # float + int = float
                    self.operators[2]: self.types[2],  # float - int = float
                    self.operators[3]: self.types[2],  # float * int = float
                    self.operators[4]: self.types[2],  # float / int = float
                    self.operators[5]: self.types[4],  # float < int = bool
                    self.operators[6]: self.types[4],  # float > int = bool
                    self.operators[7]: self.types[4],  # float <= int = bool
                    self.operators[8]: self.types[4],  # float >= int = bool
                    self.operators[9]: self.types[4],  # float == int = bool
                    self.operators[10]: self.types[4],  # float != int = bool
                    self.operators[11]: self.types[4],  # float && int = bool
                    self.operators[12]: self.types[4],  # float || int = bool
                    self.operators[13]: self.types[2],  # float = int
                    self.operators[14]: self.types[9],  # float == int = bool
                },
                
                #compatibilidad de FLOAT con FLOAT
                self.types[2]:{
                    self.operators[1]: self.types[2],  # float + float = float
                    self.operators[2]: self.types[2],  # float - float = float
                    self.operators[3]: self.types[2],  # float * float = float
                    self.operators[4]: self.types[2],  # float / float = float
                    self.operators[5]: self.types[4],  # float < float = bool
                    self.operators[6]: self.types[4],  # float > float = bool
                    self.operators[7]: self.types[4],  # float <= float = bool
                    self.operators[8]: self.types[4],  # float >= float = bool
                    self.operators[9]: self.types[4],  # float == float = bool
                    self.operators[10]: self.types[4],  # float != float = bool
                    self.operators[11]: self.types[4],  # float && float = bool
                    self.operators[12]: self.types[4],  # float || float = bool
                    self.operators[13]: self.types[2],  # float = float
                    self.operators[14]: self.types[4],  # float == float = bool    
                },
                
                #Compatibilidad de FLOAT con CHAR
                self.types[3]:{
                    self.operators[1]: self.types[9],  # float + char = ERROR
                    self.operators[2]: self.types[9],  # float - char = ERROR
                    self.operators[3]: self.types[9],  # float * char = ERROR
                    self.operators[4]: self.types[9],  # float / char = ERROR
                    self.operators[5]: self.types[9],  # float < char = ERROR
                    self.operators[6]: self.types[9],  # float > char = ERROR
                    self.operators[7]: self.types[9],  # float <= char = ERROR
                    self.operators[8]: self.types[9],  # float >= char = ERROR
                    self.operators[9]: self.types[9],  # float == char = ERROR
                    self.operators[10]: self.types[9],  # float != char = ERROR
                    self.operators[11]: self.types[4],  # float && char = bool
                    self.operators[12]: self.types[4],  # float || char = bool
                    self.operators[13]: self.types[9],  # float = char
                    self.operators[14]: self.types[9],  # float == char = bool 
                },
            
                #compatibilidad de FLOAT con BOOL
                self.types[4]:{
                    self.operators[1]: self.types[9],  # bool + bool = ERROR
                    self.operators[2]: self.types[9],  # bool - bool = ERROR
                    self.operators[3]: self.types[9],  # bool * bool = ERROR
                    self.operators[4]: self.types[9],  # bool / bool = ERROR
                    self.operators[5]: self.types[9],  # bool < bool = ERROR
                    self.operators[6]: self.types[9],  # bool > bool = ERROR
                    self.operators[7]: self.types[9],  # bool <= bool = ERROR
                    self.operators[8]: self.types[9],  # bool >= bool = ERROR
                    self.operators[9]: self.types[9],  # bool == bool = ERROR
                    self.operators[10]: self.types[9],  # bool != bool = ERROR
                    self.operators[11]: self.types[4],  # bool && bool = bool
                    self.operators[12]: self.types[9],  # bool || bool = ERROR
                    self.operators[13]: self.types[9],  # bool = bool
                    self.operators[14]: self.types[9],  # bool == bool = bool
                },
           
                #compatibilidad dfe FLOAT con CTEI
                self.types[5]:{
                    self.operators[1]: self.types[2],  # float + CTEI = float
                    self.operators[2]: self.types[2],  # float - CTEI = float
                    self.operators[3]: self.types[2],  # float * CTEI = float
                    self.operators[4]: self.types[2],  # float / CTEI = float
                    self.operators[5]: self.types[4],  # float < CTEI = bool
                    self.operators[6]: self.types[4],  # float > CTEI = bool
                    self.operators[7]: self.types[4],  # float <= CTEI = bool
                    self.operators[8]: self.types[4],  # float >= CTEI = bool
                    self.operators[9]: self.types[4],  # float == CTEI = bool
                    self.operators[10]: self.types[4],  # float != CTEI = bool
                    self.operators[11]: self.types[4],  # float && CTEI = bool
                    self.operators[12]: self.types[4],  # float || CTEI = bool
                    self.operators[13]: self.types[2],  # float = CTEI
                    self.operators[14]: self.types[9],  # float == CTEI = bool
                 },
                 

                #compatibilidad de FLOAT con CTEF
                self.types[6]:{
                    self.operators[1]: self.types[2],  # float + CTEF = float
                    self.operators[2]: self.types[2],  # float - CTEF = float
                    self.operators[3]: self.types[2],  # float * CTEF = float
                    self.operators[4]: self.types[2],  # float / CTEF = float
                    self.operators[5]: self.types[4],  # float < CTEF = bool
                    self.operators[6]: self.types[4],  # float > CTEF = bool
                    self.operators[7]: self.types[4],  # float <= CTEF = bool
                    self.operators[8]: self.types[4],  # float >= CTEF = bool
                    self.operators[9]: self.types[4],  # float == CTEF = bool
                    self.operators[10]: self.types[4],  # float != CTEF = bool
                    self.operators[11]: self.types[4],  # float && CTEF = bool
                    self.operators[12]: self.types[4],  # float || CTEF = bool
                    self.operators[13]: self.types[2],  # float = CTEF
                    self.operators[14]: self.types[4],  # float == CTEF = bool
                },
                #compatibilidad de FLOAT con CTEC
                self.types[7]:{
                    self.operators[1]: self.types[9],  # float + CTEC = ERROR
                    self.operators[2]: self.types[9],  # float - CTEC = ERROR
                    self.operators[3]: self.types[9],  # float * CTEC = ERROR
                    self.operators[4]: self.types[9],  # float / CTEC = ERROR
                    self.operators[5]: self.types[9],  # float < CTEC = ERROR
                    self.operators[6]: self.types[9],  # float > CTEC = ERROR
                    self.operators[7]: self.types[9],  # float <= CTEC = ERROR
                    self.operators[8]: self.types[9],  # float >= CTEC = ERROR
                    self.operators[9]: self.types[9],  # float == CTEC = ERROR
                    self.operators[10]: self.types[9],  # float != CTEC = ERROR
                    self.operators[11]: self.types[4],  # float && CTEC = bool
                    self.operators[12]: self.types[4],  # float || CTEC = bool
                    self.operators[13]: self.types[9],  # float = CTEC
                    self.operators[14]: self.types[9],  # float == CTEC = bool
                },
            #compatibilidad de FLOAT con CSTERING
                self.types[8]:{
                    self.operators[1]: self.types[9],  # float + CTESTRING = ERROR
                    self.operators[2]: self.types[9],  # float - CTESTRING = ERROR
                    self.operators[3]: self.types[9],  # float * CTESTRING = ERROR
                    self.operators[4]: self.types[9],  # float / CTESTRING = ERROR
                    self.operators[5]: self.types[9],  # float < CTESTRING = ERROR
                    self.operators[6]: self.types[9],  # float > CTESTRING = ERROR
                    self.operators[7]: self.types[9],  # float <= CTESTRING = ERROR
                    self.operators[8]: self.types[9],  # float >= CTESTRING = ERROR
                    self.operators[9]: self.types[9],  # float == CTESTRING = ERROR
                    self.operators[10]: self.types[9],  # float != CTESTRING = ERROR
                    self.operators[11]: self.types[4],  # float && CTESTRING = bool
                    self.operators[12]: self.types[4],  # float || CTESTRING = bool
                    self.operators[13]: self.types[9],  # float = CTESTRING
                    self.operators[14]: self.types[9],  # float == CTESTRING = bool 
                }
            },
            #3 CHAR
            self.types[3]:{
                
                #compatibilidad de CHAR con INT
                self.types[1]:{
                    self.operators[1]: self.types[9],  # char + int = ERROR
                    self.operators[2]: self.types[9],  # char - int = ERROR
                    self.operators[3]: self.types[9],  # char * int = ERROR
                    self.operators[4]: self.types[9],  # char / int = ERROR
                    self.operators[5]: self.types[9],  # char < int = ERROR
                    self.operators[6]: self.types[9],  # char > int = ERROR
                    self.operators[7]: self.types[9],  # char <= int = ERROR
                    self.operators[8]: self.types[9],  # char >= int = ERROR
                    self.operators[9]: self.types[9],  # char == int = ERROR
                    self.operators[10]: self.types[9],  # char != int = ERROR
                    self.operators[11]: self.types[4],  # char && int = bool
                    self.operators[12]: self.types[4],  # char || int = bool
                    self.operators[13]: self.types[9],  # char = int
                    self.operators[14]: self.types[9],  # char == int = bool
                },

                #compatiblidad de CHAR con FLOAT
                self.types[2]:{
                    self.operators[1]: self.types[9],  # char + float = ERROR
                    self.operators[2]: self.types[9],  # char - float = ERROR
                    self.operators[3]: self.types[9],  # char * float = ERROR
                    self.operators[4]: self.types[9],  # char / float = ERROR
                    self.operators[5]: self.types[9],  # char < float = ERROR
                    self.operators[6]: self.types[9],  # char > float = ERROR
                    self.operators[7]: self.types[9],  # char <= float = ERROR
                    self.operators[8]: self.types[9],  # char >= float = ERROR
                    self.operators[9]: self.types[9],  # char == float = ERROR
                    self.operators[10]: self.types[9],  # char != float = ERROR
                    self.operators[11]: self.types[4],  # char && float = bool
                    self.operators[12]: self.types[4],  # char || float = bool
                    self.operators[13]: self.types[9],  # char = float
                    self.operators[14]: self.types[9],  # char == float = bool
                },

                #compatiblidad de CHAR con CHAR
                self.types[3]:{
                    self.operators[1]: self.types[9],  # char + char = ERROR
                    self.operators[2]: self.types[9],  # char - char = ERROR
                    self.operators[3]: self.types[9],  # char * char = ERROR
                    self.operators[4]: self.types[9],  # char / char = ERROR
                    self.operators[5]: self.types[9],  # char < char = ERROR
                    self.operators[6]: self.types[9],  # char > char = ERROR
                    self.operators[7]: self.types[9],  # char <= char = ERROR
                    self.operators[8]: self.types[9],  # char >= char = ERROR
                    self.operators[9]: self.types[4],  # char == char = bool
                    self.operators[10]: self.types[4],  # char != char = bool
                    self.operators[11]: self.types[4],  # char && char = bool
                    self.operators[12]: self.types[4],  # char || char = bool
                    self.operators[13]: self.types[3],  # char = char
                    self.operators[14]: self.types[4],  # char == char = bool
                },

                #compatibilidad de CHAR con BOOL
                self.types[4]:{
                    self.operators[1]: self.types[9],  # char + bool = ERROR
                    self.operators[2]: self.types[9],  # char - bool = ERROR
                    self.operators[3]: self.types[9],  # char * bool = ERROR
                    self.operators[4]: self.types[9],  # char / bool = ERROR
                    self.operators[5]: self.types[9],  # char < bool = ERROR
                    self.operators[6]: self.types[9],  # char > bool = ERROR
                    self.operators[7]: self.types[9],  # char <= bool = ERROR
                    self.operators[8]: self.types[9],  # char >= bool = ERROR
                    self.operators[9]: self.types[9],  # char == bool = ERROR
                    self.operators[10]: self.types[9],  # char != bool = ERROR
                    self.operators[11]: self.types[9],  # char && bool = ERROR
                    self.operators[12]: self.types[9],  # char || bool = ERROR
                    self.operators[13]: self.types[9],  # char = bool
                    self.operators[14]: self.types[9],  # char == bool = ERROR  
                },
                
                #compatibilidad de CHAR con CTEI
                self.types[5]:{
                    self.operators[1]: self.types[9],  # char + ctei = ERROR
                    self.operators[2]: self.types[9],  # char - ctei = ERROR
                    self.operators[3]: self.types[9],  # char * ctei = ERROR
                    self.operators[4]: self.types[9],  # char / ctei = ERROR
                    self.operators[5]: self.types[9],  # char < ctei = ERROR
                    self.operators[6]: self.types[9],  # char > ctei = ERROR
                    self.operators[7]: self.types[9],  # char <= ctei = ERROR
                    self.operators[8]: self.types[9],  # char >= ctei = ERROR
                    self.operators[9]: self.types[9],  # char == ctei = ERROR
                    self.operators[10]: self.types[9],  # char != ctei = ERROR
                    self.operators[11]: self.types[4],  # char && ctei = bool
                    self.operators[12]: self.types[4],  # char || ctei = bool
                    self.operators[13]: self.types[9],  # char = ctei
                    self.operators[14]: self.types[9],  # char == ctei = bool
                },
                
                #compatibildiad de CHAR con CTEF
                self.types[6]:{
                    self.operators[1]: self.types[9],  # char + ctef = ERROR
                    self.operators[2]: self.types[9],  # char - ctef = ERROR
                    self.operators[3]: self.types[9],  # char * ctef = ERROR
                    self.operators[4]: self.types[9],  # char / ctef = ERROR
                    self.operators[5]: self.types[9],  # char < ctef = ERROR
                    self.operators[6]: self.types[9],  # char > ctef = ERROR
                    self.operators[7]: self.types[9],  # char <= ctef = ERROR
                    self.operators[8]: self.types[9],  # char >= ctef = ERROR
                    self.operators[9]: self.types[9],  # char == ctef = ERROR
                    self.operators[10]: self.types[9],  # char != ctef = ERROR
                    self.operators[11]: self.types[4],  # char && ctef = bool
                    self.operators[12]: self.types[4],  # char || ctef = bool
                    self.operators[13]: self.types[9],  # char = ctef
                    self.operators[14]: self.types[9],  # char == ctef = bool
                },
                
                #compatibilidad de CHAR con CTEC
                self.types[7]:{
                    self.operators[1]: self.types[9],  # char + CTEC = ERROR
                    self.operators[2]: self.types[9],  # char - CTEC = ERROR
                    self.operators[3]: self.types[9],  # char * CTEC = ERROR
                    self.operators[4]: self.types[9],  # char / CTEC = ERROR
                    self.operators[5]: self.types[9],  # char < CTEC = ERROR
                    self.operators[6]: self.types[9],  # char > CTEC = ERROR
                    self.operators[7]: self.types[9],  # char <= CTEC = ERROR
                    self.operators[8]: self.types[9],  # char >= CTEC = ERROR
                    self.operators[9]: self.types[9],  # char == CTEC = ERROR
                    self.operators[10]: self.types[4],  # char != CTEC = bool
                    self.operators[11]: self.types[4],  # char && CTEC = bool
                    self.operators[12]: self.types[4],  # char || CTEC = bool
                    self.operators[13]: self.types[9],  # char = CTEC
                    self.operators[14]: self.types[9],  # char == CTEC = bool
                },
                
                #compatibilidad de CHAR con CTESTRING
                self.types[8]:{
                    self.operators[1]: self.types[9],  # char + CTEString = ERROR
                    self.operators[2]: self.types[9],  # char - CTEString = ERROR
                    self.operators[3]: self.types[9],  # char * CTEString = ERROR
                    self.operators[4]: self.types[9],  # char / CTEString = ERROR
                    self.operators[5]: self.types[9],  # char < CTEString = ERROR
                    self.operators[6]: self.types[9],  # char > CTEString = ERROR
                    self.operators[7]: self.types[9],  # char <= CTEString = ERROR
                    self.operators[8]: self.types[9],  # char >= CTEString = ERROR
                    self.operators[9]: self.types[9],  # char == CTEString = ERROR
                    self.operators[10]: self.types[4],  # char != CTEString = bool
                    self.operators[11]: self.types[4],  # char && CTEString = bool
                    self.operators[12]: self.types[4],  # char || CTEString = bool
                    self.operators[13]: self.types[9],  # char = CTEString
                    self.operators[14]: self.types[9],  # char == CTEString = bool
                }
            },
       
       #4 BOOL
        self.types[4]:{
                #compatibilidad de BOOL con INT 
                self.types[1]:{
                    self.operators[1]: self.types[9],  # bool + int = ERROR
                    self.operators[2]: self.types[9],  # bool - int = ERROR
                    self.operators[3]: self.types[9],  # bool * int = ERROR
                    self.operators[4]: self.types[9],  # bool / int = ERROR
                    self.operators[5]: self.types[9],  # bool < int = ERROR
                    self.operators[6]: self.types[9],  # bool > int = ERROR
                    self.operators[7]: self.types[9],  # bool <= int = ERROR
                    self.operators[8]: self.types[9],  # bool >= int = ERROR
                    self.operators[9]: self.types[9],  # bool == int = ERROR
                    self.operators[10]: self.types[9],  # bool != int = ERROR
                    self.operators[11]: self.types[4],  # bool && int = bool
                    self.operators[12]: self.types[4],  # bool || int = bool
                    self.operators[13]: self.types[9],  # bool = int
                    self.operators[14]: self.types[9],  # bool == int = bool
                },
                
                #compatibilida de BOOL con FLOAT
                self.types[2]:{
                    self.operators[1]: self.types[9],  # bool + float = ERROR
                    self.operators[2]: self.types[9],  # bool - float = ERROR
                    self.operators[3]: self.types[9],  # bool * float = ERROR
                    self.operators[4]: self.types[9],  # bool / float = ERROR
                    self.operators[5]: self.types[9],  # bool < float = ERROR
                    self.operators[6]: self.types[9],  # bool > float = ERROR
                    self.operators[7]: self.types[9],  # bool <= float = ERROR
                    self.operators[8]: self.types[9],  # bool >= float = ERROR
                    self.operators[9]: self.types[9],  # bool == float = ERROR
                    self.operators[10]: self.types[9],  # bool != float = ERROR
                    self.operators[11]: self.types[4],  # bool && float = bool
                    self.operators[12]: self.types[4],  # bool || float = bool
                    self.operators[13]: self.types[9],  # bool = float
                    self.operators[14]: self.types[9],  # bool == float = bool
                },

                #compatibilidad de BOOL con CHAR
                self.types[3]:{
                   self.operators[1]: self.types[9],  # bool + char = ERROR
                    self.operators[2]: self.types[9],  # bool - char = ERROR
                    self.operators[3]: self.types[9],  # bool * char = ERROR
                    self.operators[4]: self.types[9],  # bool / char = ERROR
                    self.operators[5]: self.types[9],  # bool < char = ERROR
                    self.operators[6]: self.types[9],  # bool > char = ERROR
                    self.operators[7]: self.types[9],  # bool <= char = ERROR
                    self.operators[8]: self.types[9],  # bool >= char = ERROR
                    self.operators[9]: self.types[9],  # bool == char = ERROR
                    self.operators[10]: self.types[9],  # bool != char = ERROR
                    self.operators[11]: self.types[4],  # bool && char = bool
                    self.operators[12]: self.types[4],  # bool || char = bool
                    self.operators[13]: self.types[9],  # bool = char
                    self.operators[14]: self.types[9],  # bool == char = bool 
                },

                #compatibilidad de BOOL con BOOL
                self.types[4]:{
                    self.operators[1]: self.types[9],  # bool + bool = ERROR
                    self.operators[2]: self.types[9],  # bool - bool = ERROR
                    self.operators[3]: self.types[9],  # bool * bool = ERROR
                    self.operators[4]: self.types[9],  # bool / bool = ERROR
                    self.operators[5]: self.types[4],  # bool < bool = bool
                    self.operators[6]: self.types[4],  # bool > bool = bool
                    self.operators[7]: self.types[4],  # bool <= bool = bool
                    self.operators[8]: self.types[4],  # bool >= bool = bool
                    self.operators[9]: self.types[4],  # bool == bool = bool
                    self.operators[10]: self.types[4],  # bool != bool = bool
                    self.operators[11]: self.types[4],  # bool && bool = bool
                    self.operators[12]: self.types[4],  # bool || bool = bool
                    self.operators[13]: self.types[4],  # bool = bool
                    self.operators[14]: self.types[4],  # bool == bool = bool
                },
                
                #compatibiliad de BOOL con CTEI
                self.types[5]: {
                    self.operators[1]: self.types[9],  # bool + ctei = ERROR
                    self.operators[2]: self.types[9],  # bool - ctei = ERROR
                    self.operators[3]: self.types[9],  # bool * ctei = ERROR
                    self.operators[4]: self.types[9],  # bool / ctei = ERROR
                    self.operators[5]: self.types[9],  # bool < ctei = ERROR
                    self.operators[6]: self.types[9],  # bool > ctei = ERROR
                    self.operators[7]: self.types[9],  # bool <= ctei = ERROR
                    self.operators[8]: self.types[9],  # bool >= ctei = ERROR
                    self.operators[9]: self.types[9],  # bool == ctei = ERROR
                    self.operators[10]: self.types[9],  # bool != ctei = ERROR
                    self.operators[11]: self.types[4],  # bool && ctei = bool
                    self.operators[12]: self.types[4],  # bool || ctei = bool
                    self.operators[13]: self.types[9],  # bool = ctei
                    self.operators[14]: self.types[9],  # bool == ctei = bool
                },
                
                #compatibilidad de BOOL con CTEF
                self.types[6]: {
                    self.operators[1]: self.types[9],  # bool + ctef = ERROR
                    self.operators[2]: self.types[9],  # bool - ctef = ERROR
                    self.operators[3]: self.types[9],  # bool * ctef = ERROR
                    self.operators[4]: self.types[9],  # bool / ctef = ERROR
                    self.operators[5]: self.types[9],  # bool < ctef = ERROR
                    self.operators[6]: self.types[9],  # bool > ctef = ERROR
                    self.operators[7]: self.types[9],  # bool <= ctef = ERROR
                    self.operators[8]: self.types[9],  # bool >= ctef = ERROR
                    self.operators[9]: self.types[9],  # bool == ctef = ERROR
                    self.operators[10]: self.types[9],  # bool != ctef = ERROR
                    self.operators[11]: self.types[4],  # bool && ctef = bool
                    self.operators[12]: self.types[4],  # bool || ctef = bool
                    self.operators[13]: self.types[9],  # bool = ctef
                    self.operators[14]: self.types[9],  # bool == ctef = bool
                },
                     
                #compatibilidad de BOOl con CTEC    
                self.types[7]: {
                    self.operators[1]: self.types[9],  # bool + ctec = ERROR
                    self.operators[2]: self.types[9],  # bool - ctec = ERROR
                    self.operators[3]: self.types[9],  # bool * ctec = ERROR
                    self.operators[4]: self.types[9],  # bool / ctec = ERROR
                    self.operators[5]: self.types[9],  # bool < ctec = ERROR
                    self.operators[6]: self.types[9],  # bool > ctec = ERROR
                    self.operators[7]: self.types[9],  # bool <= ctec = ERROR
                    self.operators[8]: self.types[9],  # bool >= ctec = ERROR
                    self.operators[9]: self.types[9],  # bool == ctec = ERROR
                    self.operators[10]: self.types[9],  # bool != ctec = ERROR
                    self.operators[11]: self.types[4],  # bool && ctec = bool
                    self.operators[12]: self.types[4],  # bool || ctec = bool
                    self.operators[13]: self.types[9],  # bool = ctec
                    self.operators[14]: self.types[9],  # bool == ctec = bool
                },
                
                #compatibilidad de BOOL con CTEC
                self.types[8]: {
                    self.operators[1]: self.types[9],  # ctestring + ctec = ERROR
                    self.operators[2]: self.types[9],  # ctestring - ctec = ERROR
                    self.operators[3]: self.types[9],  # ctestring * ctec = ERROR
                    self.operators[4]: self.types[9],  # ctestring / ctec = ERROR
                    self.operators[5]: self.types[9],  # ctestring < ctec = ERROR
                    self.operators[6]: self.types[9],  # ctestring > ctec = ERROR
                    self.operators[7]: self.types[9],  # ctestring <= ctec = ERROR
                    self.operators[8]: self.types[9],  # ctestring >= ctec = ERROR
                    self.operators[9]: self.types[9],  # ctestring == ctec = ERROR
                    self.operators[10]: self.types[9],  # ctestring != ctec = ERROR
                    self.operators[11]: self.types[4],  # ctestring && ctec = bool
                    self.operators[12]: self.types[4],  # ctestring || ctec = bool
                    self.operators[13]: self.types[9],  # ctestring = ctec
                    self.operators[14]: self.types[9],  # ctestring == ctec = bool
            },    
        }

        }

    def getType(self, lf, rg, op):
        return self.dance[lf][rg][op]
            
    def pr(self,lf,rg,op):
        print('valor de retorno es->', self.getType(lf, rg, op))

  
