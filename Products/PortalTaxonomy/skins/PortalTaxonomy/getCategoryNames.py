from Products.CMFCore.utils import getToolByName
returned = []

# use the attribute (uid) to fetch the names (title)
cats = context['getCategories']

pc = getToolByName(context,'portal_catalog')
query = {}
query['portal_type'] = 'Category'
query['review_state'] = 'public'
query['UID'] = cats
query['sort_on'] = 'sortable_title'

results = pc.searchResults(query)

if not results:
    return returned

for result in results:
    pair = []
    pair.append(result.Title)
    pair.append(result.UID)
    returned.append(pair)

return returned
