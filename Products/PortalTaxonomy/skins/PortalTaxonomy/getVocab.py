from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import DisplayList

pc = getToolByName(context,'portal_catalog')

query = {}
portal_path = context.portal_url.getPortalPath()
query['path'] = portal_path
query['portal_type'] = 'Category'
query['review_state'] = 'public'
#query['sort_on'] = 'getObjPositionInParent'

categories = {}
results = pc.searchResults(query)

if not results:
    return [], []

cats = [cat for cat in results]
cats.sort(lambda x, y: cmp(len(x.getPath()), len(y.getPath())))

for result in cats:
    path_str = result.getPath()
    path = path_str.split('/')
    parent_path = path[:-1]
    parent_path_str = '/'.join(parent_path)
    data = {'UID': result.UID,
        'Title': result.Title,
        'children': [],
    }

    if categories.has_key(parent_path_str):
        categories[parent_path_str]['children'].append(path_str)

    categories[path_str] = data

# Get Parent Categories
vocab = []
catman = getToolByName(context, 'portal_categories')
for path in categories.keys():
    parent_path = '/'.join(path.split('/')[:-1])
    if categories.has_key(parent_path):
        continue
    data = categories.get(path)
    children = catman.getAllChildren(categories,data['children'])
    children.sort(lambda x, y: cmp(x[1], y[1]))
    vocab.append((data['UID'],data['Title'],children))
display_list = DisplayList()
for c in results:
    display_list.add(c.UID, c.Title)
return vocab, display_list
