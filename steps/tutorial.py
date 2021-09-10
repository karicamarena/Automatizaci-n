from behave import *
import requests

@When('I request GET')
def step_impl(context):
   context.resp = requests.get("https://dog.ceo/api/breeds/list/all")
  
    


@then('I should receive an OK  response')
def step_impl(context):
   assert context.resp.status_code == 200 
   assert context.resp.json()
   print(context.resp)

   @then ('I check that response contains property')
   def step_impl(context):
          assert.resp.json() ['message'] == 'akita'

   

	
	


    
# Corregir que sea un when en lugar de given 
# jupyter nootebook 
# Hacia http bin hacer un llamado.
#Que quiero automatizar??? 
#Tratar de hacer un ejemplo. 
#MiCuaderno esta en C:\Users\xmy2329\Documents\codePython


