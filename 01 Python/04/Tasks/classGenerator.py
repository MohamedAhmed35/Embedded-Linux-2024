import datetime



name = str(input("please enter your name: "))
className = str(input('please enter class name: '))
nameSpace = str(input('please enter name space: '))
x = datetime.datetime.now()

copyRight_sec = rf'''
/***************************************************************
 *                                                             * 
 *                                                             * 
 *                     CopyRight {name}{'*'.rjust(31-len(name))}   
 *                                                             * 
 *                                                             * 
 ***************************************************************/
'''

doc_sec = rf"""
/*
autor: {name}
data : {x.strftime("%a %b %d %I:%M:%S %p %Y")}
breif:
*/
"""

nameSpace_def = rf"""
namespace {nameSpace} 
{{
    class {className}
    {{
        public:
            {className}();
            ~{className}();
        private:
    }};
}}"""


nameSpace_dec = rf"""
namespace {nameSpace}
{{
    {className}::{className}(){{}}
    {className}::~{className}(){{}}
}}"""


include_sec = rf"""
#include "{className}.hpp" 
"""

with open(f'{className}.cpp', 'w') as file:
    file.write(copyRight_sec + doc_sec + include_sec + nameSpace_dec)
    
with open(f'{className}.hpp', 'w') as file:
    file.write(copyRight_sec + doc_sec + nameSpace_def)
