package com.wimt_hackathon.SmartDocs.services;

import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;


public class SmartDocsService {

    public void centralControl(){
    // Step 1: Scan Emails and Extract Attachments
       EmailScanner.scanEmails();

       // Placeholder InputStream (Replace with actual stream from email attachments)
       InputStream documentStream = getDocumentStreamFromEmail();

       // Step 2: Extract Document Text
       String extractedText = DocumentProcessor.extractText(documentStream);

       // Step 3: NLP Extraction of Key Information
       NlpExtractor nlpExtractor;
       try {
           nlpExtractor = new NlpExtractor();
           String[] names = nlpExtractor.extractNames(extractedText);
           System.out.println("Extracted Names: " + Arrays.toString(names));
       } catch (Exception e) {
           e.printStackTrace();
       }

       // Step 4: Populate Template
       String template = "Dear {{ClientName}},\nYour account number {{AccountNumber}} is ready for processing.";
       TemplateProcessor templateProcessor = new TemplateProcessor(template);
       Map<String, String> values = new HashMap<>();
       values.put("ClientName", "John Doe");
       values.put("AccountNumber", "123456");

       String populatedTemplate = templateProcessor.populateTemplate(values);

       // Step 5: Route Document
       WorkflowRouter router = new WorkflowRouter();
       router.routeDocument(populatedTemplate, "financial_statement");
   }

   private static InputStream getDocumentStreamFromEmail() {
       // Placeholder for document stream from Email Scanner
       return null;
   }

}
