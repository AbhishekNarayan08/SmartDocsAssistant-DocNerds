package com.wimt_hackathon.SmartDocs.services;

public class WorkflowRouter {
    public void routeDocument(String populatedTemplate, String documentType) {
        if (documentType.equalsIgnoreCase("tax_form")) {
            sendToTeam("Tax Team", populatedTemplate);
        } else if (documentType.equalsIgnoreCase("financial_statement")) {
            sendToTeam("Finance Team", populatedTemplate);
        }
        // Add more routing logic as needed
    }

    private void sendToTeam(String teamName, String documentContent) {
        System.out.println("Routing to: " + teamName);
        System.out.println("Document Content: \n" + documentContent);
        // Implement the routing logic, e.g., send an email, save to database, etc.
    }
}
