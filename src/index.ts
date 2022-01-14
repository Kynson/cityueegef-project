// @ts-ignore TS2724 'blockly' has no exported member 'Themes' 
import { inject, Theme, Themes, Blocks } from 'blockly';
import Python from 'blockly/python';

const theme = Theme.defineTheme('test', {
  base: Themes.Dark,
  componentStyles: {
    workspaceBackgroundColour: '#121212'
  }
});

const deployButton = document.getElementById('deploy');

const workspace = inject('blockly-main-container', {toolbox: document.getElementById('toolbox'), sounds: false, theme});

Blocks['has_faces'] = {
  init: function() {
    this.setOutput(true, 'Boolean');
    this.appendDummyInput()
      .appendField('has_faces');
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Python['has_faces'] = function() {
  const code = 'has_faces()';
  return [code, 2.2];
};

Blocks['recognize_face'] = {
  init: function() {
    this.setOutput(true, 'Tuple');
    this.appendDummyInput()
      .appendField('recognize_face');
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Python['recognize_face'] = function() {
  const code = 'recognize_face()';
  return [code, 2.2];
};

deployButton.addEventListener('click', () => {
  console.log(Python.workspaceToCode(workspace))
});