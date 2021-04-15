


class GenerateBulkImportUseCase(object):
    company = None
    data = None

    def __init__(self, company, data):
       self.company = company
       self.data = data

    def run(self):
        splitted_data = self._split_data_per_users()
        from user_list_of_customers in splitted_data:
            HTTPRequest(url:"subtask_bulk_import.badgermapping.com", params:{data:user_list_of_customers, user: user, bulk_import_id:bulk_import_id} )

    def _split_data_per_users(self):
        pass
        #take line by line the file and split in an array of arrays
        #splitting customers by user