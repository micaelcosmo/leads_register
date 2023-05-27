from fastapi import FastAPI
from crud import create_item, read_item, update_item, delete_item

app = FastAPI()


@app.post('/items')
def create(request):
    item = request.json()
    create_item(item)
    return {'message': 'Item created successfully'}


@app.get('/items/{item_id}')
def read(item_id):
    item = read_item(item_id)
    return {'item': item}


@app.put('/items/{item_id}')
def update(item_id, request):
    updated_item = request.json()
    update_item(item_id, updated_item)
    return {'message': 'Item updated successfully'}


@app.delete('/items/{item_id}')
def delete(item_id):
    delete_item(item_id)
    return {'message': 'Item deleted successfully'}
