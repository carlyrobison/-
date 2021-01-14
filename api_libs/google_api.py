from googleapiclient.discovery import build
from google.oauth2 import service_account
import settings as settings


_credentials = service_account.Credentials.from_service_account_info(
	settings.GOOGLE_API_AUTHN_INFO,
    scopes=settings.GOOGLE_DRIVE_PERMISSIONS_SCOPES,
)

def sheets_service():
    return build(
        "sheets", "v4", credentials=_credentials, cache_discovery=False
    )

def drive_service():
    return build(
        "drive", "v3", credentials=_credentials, cache_discovery=False
    )

def make_sheet(name):

        # template = (
        #     self.drive_service()
        #     .files()
        #     .get(fileId=settings.GOOGLE_SHEETS_TEMPLATE_FILE_ID, fields="owners")
        #     .execute()
        # )
        # self._sheets_owner = template["owners"][0]["emailAddress"]

    req_body = {"name": name}
    # copy template sheet
    file = drive_service().files().copy(
            fileId=settings.GOOGLE_SHEETS_TEMPLATE_FILE_ID,
            body=req_body,
            fields="id,webViewLink,permissions",
        ).execute()
    return file

	# spreadsheet = {
	#     'properties': {
	#         'title': 'title goes here'
	#     }
	# }
	# spreadsheet = sheets_service().spreadsheets().create(body=spreadsheet,
 #                                    fields='spreadsheetId').execute()
	# print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
	# return spreadsheet.get('url')


