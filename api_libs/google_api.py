from googleapiclient.discovery import build
from google.oauth2 import service_account
import settings as settings


# helper
def extract_id_from_sheets_url(url):
    """
    Assumes `url` is of the form
    https://docs.google.com/spreadsheets/d/<ID>/edit...
    and returns the <ID> portion
    """
    start = url.find("/d/") + 3
    end = url.find("/edit")
    return url[start:end]

class GoogleDriveAPI:
    def __init__(self):
        if settings.GOOGLE_API_AUTHN_INFO is None:
            print('No google drive integration!')
        self._credentials = service_account.Credentials.from_service_account_info(
            settings.GOOGLE_API_AUTHN_INFO,
            scopes=settings.GOOGLE_DRIVE_PERMISSIONS_SCOPES,
        )

    def sheets_service(self):
        return build(
            "sheets", "v4", credentials=self._credentials, cache_discovery=False
        )

    def drive_service(self):
        return build(
            "drive", "v3", credentials=self._credentials, cache_discovery=False
        )

    def add_puzzle_link_to_sheet(self, puzzle_url, sheet_id):
        req_body = {
            "values": [
                [f'=HYPERLINK("{puzzle_url}", "Puzzle Link")'],
            ]
        }
        self.sheets_service().spreadsheets().values().update(
            spreadsheetId=sheet_id,
            range="C1:C1",
            valueInputOption="USER_ENTERED",
            body=req_body,
        ).execute()

    def make_sheet(self, name, puzzle_url=''):
        req_body = {"name": name}
        # copy template sheet
        file = self.drive_service().files().copy(
                fileId=settings.GOOGLE_SHEETS_TEMPLATE_FILE_ID,
                body=req_body,
                fields="id,webViewLink,permissions",
            ).execute()
        print(file)
        sheet_url = file["webViewLink"]

        if puzzle_url != '':
            self.add_puzzle_link_to_sheet(puzzle_url, file["id"])

        return sheet_url


	# spreadsheet = sheets_service().spreadsheets().create(body=spreadsheet,
 #                                    fields='spreadsheetId').execute()
	# print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
	# return spreadsheet.get('url')


# IGNORING CODE
# transfer new sheet ownership back to OG owner, so that scripts can run
def transfer_ownership(file):
    permission = next(
        p for p in file["permissions"] if p["emailAddress"] == self._sheets_owner
    )
    self.drive_service().permissions().update(
        fileId=file["id"],
        permissionId=permission["id"],
        body={"role": "owner"},
        transferOwnership=True,
    ).execute()
