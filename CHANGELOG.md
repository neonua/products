1) Add files to gitignor
2) Changed readme.md
3) Fixed and changed models.py:
    - change pk in Product
    - fixed creating slug
    - add 'auto_now=True' to modified_at
    - add 'auto_now_add=True' to created_at
    - add get_absolute_url
    
4) Changed admin.py:
    - another way to create 'view_on_site'

5) Changed views.py:
    - in 'like' removed request to Product
    - in 'product_simple' fixed error when check liked post or not
    - in 'product_simple' used timezone
    
6) Add unit-tests
