#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehumancommunity.org/

**Github Code Home Page:**    https://github.com/makehumancommunity/

**Authors:**           Glynn Clements

**Copyright(c):**      MakeHuman Team 2001-2019

**Licensing:**         AGPL3

    This file is part of MakeHuman (www.makehumancommunity.org).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Abstract
--------

Lightmap texture exporter
"""

from export import Exporter

class ExporterLight(Exporter):
    def __init__(self):
        Exporter.__init__(self)
        self.group = "map"
        self.name = "Lightmap"
        self.filter = "PNG (*.png)"

    def build(self, options, taskview):
        import gui
        pass

    def export(self, human, filename):
        import projection

        dstImg = projection.mapLighting()
        filepath = filename("png")
        dstImg.save(filepath)

    def onShow(self, exportTaskView):
        exportTaskView.scaleBox.hide()

    def onHide(self, exportTaskView):
        exportTaskView.scaleBox.show()


def load(app):
    app.addExporter(ExporterLight())

def unload(app):
    pass

