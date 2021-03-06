"""
JEB Decompiler (c) PNF Software, Inc.

This sample script is to be run in a UI context, such as within the JEB desktop client.
It will focus the first view found to contain a fragment named 'Disassembly', and select+focus that fragment.

Refer to SCRIPTS.TXT for more information.
"""

from com.pnfsoftware.jeb.client.api import IScript

def getDisassemblyFragment(view):
  for fragment in view.getFragments():
    if view.getFragmentLabel(fragment) == 'Disassembly':
      return fragment

def focusDisassemblyFragment(ctx):
  for view in ctx.getViews():
    fragment = getDisassemblyFragment(view)
    if fragment:
      view.setFocus()
      view.setActiveFragment(fragment)
      return True
  return False

class FocusDisas(IScript):
  def run(self, ctx):
    success = focusDisassemblyFragment(ctx)
    print('Focused Disassembly fragment: %s' % success)
