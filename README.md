# Volná místa 

- skript pro stahování volných pozic z webových stránek českých ministerstev
- velmi hrubá verze
- optimalizováno pro morph.io
- v současné době nestahuje MŽP

## To do - presenation

- [ ] improve documentation - scope and intent

## To do - scope

- [ ] add MZP
- [ ] add CSSZ (should be easy)
- [ ] add NKU (should be easy)
- [ ] add FU/FS (could use new functionality - pagination and multi-element titles)
- [ ] add UP (requires use new functionality - different-element title and url)
- [ ] add UOOZ (requires new functionality - link-less jobs)
- [ ] add CUZK
- [ ] add Hygiena
- [x] add MZV

## To do - technical

- [ ] programmatically allow for link-less jobs (linking only to general jobs page)
- [ ] add fallback for when nothing is found
- [ ] implement getting title and url from different elements
- [ ] implement getting title from multiple elements
- [ ] implement programmatic pagination
- [ ] add error handling
- [ ] rewrite scraper routine to take whole dict item as input and deal with the rest
- [ ] merge the two input dictionaries
- [ ] document data model for input parameters
- [ ] place input data into external json files
- [ ] scope out list of bodies
- [ ] save first-seen and last-seen dates + implement updating instead of duplication
- [x] add fallback for when page not found (e.g. second page of results)
- [x] resolve MD HTTP issue

## Links

- Scraper a možnost stažení dat: https://morph.io/petrbouchal/GovJobsCZ
- Shiny app: http://petrbouchal.shinyapps.io/czjobs
- Shiny app na webu Byrokrates: http://byrokrates.cz/praceprostat

## Documentation

### Data model for input parameters

Each organisation has two entries:

1. Basic listing entered as a dictionary entry, with a list as the value

Data model for dictionary entry:

    'Abbrev' = [HumanFriendlyAbbrev (str), FullName (str), HomePageUrl (str), JobPageUrl (str)]

2. Detailed input parameters as dictionary entry, with a list as the value

Data model for dictionary entry:

    'Abbrev' = [grabSubitems? (bool), # search for sub-element when iterating through jobs?
                layer1spec (dict), #
                layer2spec (dict),
                itemspec (dict),
                subitem (dict),
                separateURLelement? (bool),
                itemspec (dict),
                noJobURL (bool),
                additionalTitleText? (bool),
                itemspec (dict),
                paginate? (bool),
                pagLayer1spec (dict),
                pagLayer2spec (dict),
                pagURLitemSpec (dict)]

But perhaps the whole structure should be changed to a dictionary so the scraping routine can rely on named arguments instead of order. If not, it will need to be reordered to put the boolean switches first.



