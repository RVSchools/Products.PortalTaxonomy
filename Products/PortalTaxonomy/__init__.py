"""
------------------------------------------------------------------------------
Name:         __init__.py
Purpose:      Zope product init file
Author:       Jeremy Stark <jeremy@deximer.com>
Copyright:    (c) 2004 by Deximer, Inc.
Licence:      GNU General Public Licence (GPL) Version 2 or later
------------------------------------------------------------------------------
"""
try:
    import plone.app.upgrade
    plone.app.upgrade #pyflakes
    PLONE4 = True
except ImportError:
    PLONE4 = False

from Products.CMFCore import utils, DirectoryView

from Products.Archetypes.public import *
from Products.Archetypes import listTypes
from Permissions import ContentPermissionMap

from Products.PortalTaxonomy.ContentInitHack import separateTypesByPerm


PROJECTNAME = "PortalTaxonomy"


product_globals=globals()


DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/PortalTaxonomy', product_globals)


def initialize(context):
    from Products.PortalTaxonomy.content import CategoryManager
    from Products.PortalTaxonomy.content import Category
    from Products.PortalTaxonomy.content import AttributeManager
    from Products.PortalTaxonomy.content import AttributeCollection
    from Products.PortalTaxonomy.content import Attribute
    from Products.PortalTaxonomy import fields
    from Products.PortalTaxonomy import widgets
    from Products.PortalTaxonomy import examples

    the_types = listTypes(PROJECTNAME)
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    tools=[ CategoryManager
	  , AttributeManager
          ]
    utils.ToolInit( PROJECTNAME+' Tools'
                  , tools = tools
                  , product_name = PROJECTNAME
                  , icon='tool.gif'
                   ).initialize( context )

    type_map = separateTypesByPerm(
        the_types,
	content_types,
	constructors,
	ContentPermissionMap
	)

    i=0
    for permission in type_map:
        factory_info = type_map[ permission ]
        content_types = tuple([fi[0] for fi in factory_info])
        constructors  = tuple([fi[1] for fi in factory_info])

        utils.ContentInit( PROJECTNAME + ' Content %d' % i
                         , content_types = content_types
                         , permission = permission
                         , extra_constructors = constructors
                         , fti = ftis
                         ).initialize(context)

#    if CustomizationPolicy and hasattr(CustomizationPolicy,'register'):
#        CustomizationPolicy.register(context)
