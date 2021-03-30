'''
    Copyright 2021 Leap Australia Pty Ltd

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Author:
    Nish Joseph
'''
from os import environ

PROJECT_KEY = 'KkVJeAWXLJOAiTrq'


clr.AddReference("Ans.UI.Toolkit")
clr.AddReference("Ans.UI.Toolkit.Base")
import Ansys.UI.Toolkit as AnsysTk


class ElasticProjectNameForm(AnsysTk.Dialog):
    def __init__(self, current_id):
        self.CurrentId = current_id
        self._ButtonOkay =AnsysTk.Button()
        self._ProjLab = AnsysTk.Label()
        self._ProjNameInp = AnsysTk.TextBox()

        self.ClientSize = AnsysTk.Drawing.Size(440, 85)
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.Name = "ElasticProjectNameForm"
        self.Text = "Elastic Project Info"

        self._build_ui()
        self._ButtonOkay.Click += AnsysTk.EventDelegate(self._button_click_ok)
        
        self.Controls.Add(self._ButtonOkay)
        self.Controls.Add(self._ProjLab)
        self.Controls.Add(self._ProjNameInp)
    
    def _build_ui(self):

        self._ButtonOkay.Location =  AnsysTk.Drawing.Point(350, 50)
        self._ButtonOkay.Name = "ButtonOkay"
        self._ButtonOkay.Size = AnsysTk.Drawing.Size(75, 25)
        self._ButtonOkay.Text = "OK"

        self._ProjLab.Location = AnsysTk.Drawing.Point(15, 10)
        self._ProjLab.Name = "ProjLabel"
        self._ProjLab.Size = AnsysTk.Drawing.Size(125, 25)
        self._ProjLab.Text = "Elastic Project ID"

        self._ProjNameInp.Location = AnsysTk.Drawing.Point(145, 10)
        self._ProjNameInp.Name = "ProjNameInp"
        self._ProjNameInp.Size = AnsysTk.Drawing.Size(285, 25)
        if self.CurrentId:
            self._ProjNameInp.Text = self.CurrentId
    
    def _button_click_ok(self, sender, args):
        ExtAPI.Extension.Attributes[PROJECT_KEY] = self._ProjNameInp.Text
        self.Hide()

def set_enviroment():
    environ['ANSYS_ELASTIC_PROJECT'] = ExtAPI.Extension.Attributes[PROJECT_KEY]


def get_set_project(context):
    '''
    Callback on every context
    '''
    if context == 'Project':
        if not ExtAPI.Extension.Attributes.Contains(PROJECT_KEY):
            ExtAPI.Extension.Attributes[PROJECT_KEY] = None    
        else:
            set_enviroment()

def set_project_id(temp):
    with ElasticProjectNameForm(ExtAPI.Extension.Attributes[PROJECT_KEY]) as app:
        app.ShowDialog()
    set_enviroment()

