# This Program will automatically make components for React 

import sys
from string import Template
import os

path = r'./'

print(os.listdir(path))


def main():
  
  components = sys.argv[1:]
  for component in components:
    create_components(component)

  create_export()
                
 

def create_components(component):
  snippet = Template("""
const $name = () => {
  return (
    <div>
      
    </div>
  );
};

export default $name;
""")

  code = snippet.substitute(name = component)
  filename = component + '.jsx'
  file = open(filename, 'w')
  file.write(code)
  file.close()


def create_export():
  path = r'./'
  files = os.listdir(path)
  import_template = Template("import $name from $name;\n")
  export_template = '''
export {
          '''
  code = ''
  for file in files:
    if file.endswith('.jsx'):
      file = file.split('.')
      file = file[0]
      code += import_template.substitute(name = file)
      export_template +=  file + ',\n'
  export_template += '}'
  code += export_template

  file = open('export.js', 'w')
  file.write(code)
  file.close()


if __name__ == '__main__':
  main()