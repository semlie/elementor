import unittest
import apiClient
import virustotal
import storage

class MyTestCase(unittest.TestCase):
    # def test_build_id(self):
    #     r= apiClient.get_url_id('fourthgate.org/Yryzvt')
    #     self.assertEqual(True, r not in [''])
    #
    #
    # def test_get(self):
    #     # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
    #     r= apiClient._get( apiClient.build_url('www.elementor.com'))
    #     self.assertEqual(True, r not in [''])
    #
    #
    # def test_extract_cat(self):
    #     # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
    #     r= apiClient._get( apiClient.build_url('www.elementor.com'))
    #     res =virustotal.process_vote_results(r)
    #     cat= res[1]
    #     self.assertEqual(True, r not in [''])
    #
    def test_extract_vote_elementor(self):
        # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
        r= apiClient._get( apiClient.build_url('www.elementor.com'))
        res =virustotal.process_vote_results(r)
        vote =res[0]
        self.assertEqual(False, vote)

    # def test_extract_vote_fourthgate(self):
    #     # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
    #     r= apiClient._get( apiClient.build_url('fourthgate.org'))
    #     self.assertTrue(r.status_code==200)
    #     res =virustotal.process_vote_results(r)
    #     vote =res[0]
    #     self.assertEqual(True, vote)
  # def test_extract_vote_fourthgate(self):
  #       # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
  #       db = storage.DB()
  #       result =db.update("REPLACE INTO sites (url, risk) VALUES('www.elementor.com',0)")
  #       self.assertEqual(True, result)
  #   def test_db_select(self):
  #       row={"url":'www.elementor.com','risk':0}
  #
  #       # r= apiClient.get( apiClient.build_url('fourthgate.org/Yryzvt'))
  #       db = storage.DB()
  #       s= "select * from site"
  #       # s= "select * from 'site' where url = 'www.elementor.com'"
  #       result =db._select(s)
  #       self.assertEqual(True, result)
  #



if __name__ == '__main__':
    unittest.main()
