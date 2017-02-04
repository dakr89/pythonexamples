from bs4 import BeautifulSoup
import pandas as pd
# fb = open('resume_w_xsl.xml','r')
# soup = BeautifulSoup(fb,'lxml-xml')
# tag = soup.find_all('client')
# # getting links and location from xml file
# local = []
# links = []
# if len(tag):
# 	for x in tag:
# 		local.append(x.get('location'))
# 		links.append(x.get('www'))


# keywords = soup.find_all('keywords')

# keyword= []
# if len(keywords):
# 	for x in keywords:
# 		keyword.append(x.get('list'))


# project = soup.find_all('project')		
# start= []
# end = []
# if len(project):
# 	for x in project:
# 		start.append(x.get('start'))
# 		end.append(x.get('end'))
		
# df = pd.DataFrame(local, columns=['location'])
# df['website'] = pd.DataFrame(links)
# df['keywords'] = pd.DataFrame(keyword)
# df['start'] = pd.DataFrame(start)
# df['end'] = pd.DataFrame(end)


# file1 = open('file1.xml','r')

soup = BeautifulSoup(open("file1.xml"))
pub_ref = soup.find_all('publication-reference')


pub_ref_doc_id_cntry = []
pub_ref_doc_id_doc_number = []
pub_ref_doc_id_kind = []
pub_ref_doc_id_date = []

for tag_value in pub_ref:
	pub_ref_doc_id_cntry.append(tag_value.find('document-id').find('country').text)
	pub_ref_doc_id_doc_number.append(tag_value.find('document-id').find('doc-number').text)
	pub_ref_doc_id_kind.append(tag_value.find('document-id').find('kind').text)
	pub_ref_doc_id_date.append(tag_value.find('document-id').find('date').text)



app_ref = soup.find_all('application-reference')

app_ref_apl_type = []
app_ref_doc_id_cntry = []
app_ref_doc_id_doc_number = []
app_ref_doc_id_date = []

for tag_value in app_ref:
	app_ref_apl_type.append(tag_value.get('appl-type'))
	app_ref_doc_id_cntry.append(tag_value.find('document-id').find('country').text)
	app_ref_doc_id_doc_number.append(tag_value.find('document-id').find('doc-number').text)
	app_ref_doc_id_date.append(tag_value.find('document-id').find('date').text)
	

us_app_ser = soup.find_all('us-application-series-code')
us_app_ser_code = []

for tag_value in us_app_ser:
	us_app_ser_code.append(tag_value.text)



assignees = soup.find_all('assignees')
assign_assine_adr_org = []
assign_assine_adr_role = []
assign_assine_adr_city = []
assign_assine_adr_state = []
assign_assine_adr_country = []

for tag_value in assignees:
	assign_assine_adr_org.append(tag_value.find('assignee').find('addressbook').find('orgname').text)
	assign_assine_adr_role.append(tag_value.find('assignee').find('addressbook').find('role').text)
	assign_assine_adr_city.append(tag_value.find('assignee').find('addressbook').find('address').find('city').text)
	assign_assine_adr_state.append(tag_value.find('assignee').find('addressbook').find('address').find('city').text)
	assign_assine_adr_country.append(tag_value.find('assignee').find('addressbook').find('address').find('country').text)



#  invention title and id 
invention = soup.find_all('invention-title')
invention_title = []
invention_id = []

for tag_value in invention:
	invention_title.append(tag_value.text)
	invention_id.append(tag_value.get('id'))


