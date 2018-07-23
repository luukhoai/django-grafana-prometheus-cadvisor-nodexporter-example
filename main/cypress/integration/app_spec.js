describe("Django REST framework / React quickstart app", () => {
  const snippet = {
    title: "Title 1",
    code: "Code 1"
  };

  before(() => {
//    cy.exec("npm run build");
//    cy.exec("npm run flush");
  });

  it("should be able to fill a web form", () => {
    cy.visit("/");

    cy
      .get('input[name="title"]')
      .type(snippet.title)
      .should("have.value", snippet.title);

    cy
      .get('input[name="code"]')
      .type(snippet.code)
      .should("have.value", snippet.code);

    cy.get('.reactjs-form').submit();
  });

  it("should be able to see the table", () => {
    cy.visit("/");
    cy.get("tr").contains(`${snippet.title}${snippet.code}`);
  });
});
