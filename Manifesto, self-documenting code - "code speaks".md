# CODE SPEAKS

## The Enemy

Every comment in your codebase is an admission of defeat.

A comment says: "I couldn't make this clear enough in code, so here's what I really meant."

Comments lie. They drift from reality. They don't break tests when they become false. They don't throw errors when they contradict the code. They become lies you tell yourself and others.

```python
# The comment says one thing...
# Calculate 15% discount for premium users
discount = price * 0.2  # But the code does another
```

Code cannot lie. Code is truth. Make the code speak truth so clearly that no comment can improve it.

## The Test

A new developer should understand not just *what* your code does, but *why* it exists and *how* it fits into the business domain—all without reading a single comment.

If you cannot pass this test, you have failed.

## The Four Exceptions

There are exactly four situations where comments are acceptable:

| Type | Purpose | Example |
|------|---------|---------|
| **WHY** | Non-obvious business logic | `// California law AB-123 requires 2.5x rate for 7th consecutive day` |
| **WARNING** | Dangerous operations | `// WARNING: Bypasses all ORM validations and audit logging` |
| **TODO** | With ticket numbers | `// TODO: Remove after v1 API migration (JIRA-4521)` |
| **LEGAL** | License headers | When required by compliance |

If your comment doesn't fit these categories, rewrite your code.

## The Building Blocks

### Names That Tell Stories

Names are your most powerful tool. They should reveal intent, not implementation.

| Weak | Strong |
|------|--------|
| `get_data(id)` | `fetch_positive_balance_transactions_for_user(user_id)` |
| `check(u, p)` | `is_premium_user_recently_active(user)` |
| `proc(d)` | `calculate_discounted_prices_for_eligible_orders(orders)` |

### Functions as Sentences

Your code should read like prose:

```python
class OrderFulfillmentService:
    def fulfill_customer_order(self, order):
        self.validate_order_completeness(order)
        self.reserve_inventory_items(order)
        self.calculate_final_pricing(order)
        self.process_customer_payment(order)
        self.schedule_shipment(order)
        self.send_confirmation_email(order)
```

This code tells you the entire business process. No comments needed.

### Constants That Explain the Business

Never use magic numbers or strings. Every constant should teach domain knowledge.

| Before | After |
|--------|-------|
| `if user.account_age_days > 90 and user.purchase_count > 5:` | `LOYALTY_PROGRAM_MINIMUM_AGE_DAYS = 90`<br>`LOYALTY_PROGRAM_MINIMUM_PURCHASES = 5` |
| `apply_discount(0.1)` | `LOYALTY_PROGRAM_DISCOUNT_RATE = 0.1`<br>`apply_discount(LOYALTY_PROGRAM_DISCOUNT_RATE)` |

### Structure That Mirrors Mental Models

Your code organization should match how domain experts think:

```python
class MortgageApplication:
    def process(self):
        credit_report = self._pull_credit_report()

        if not self._meets_minimum_credit_requirements(credit_report):
            return self._decline_with_credit_counseling_resources()

        debt_to_income = self._calculate_debt_to_income_ratio()

        if self._requires_manual_underwriting(debt_to_income):
            return self._route_to_underwriter()

        return self._generate_automated_loan_offer()
```

The method structure teaches the business process.

## Patterns for Domain Teaching

### Business Rules as Objects

Transform complex conditionals into named concepts:

```python
# Before: Buried business logic
if (customer.lifetime_value > 10000 and customer.years_active > 2
    and customer.support_tickets < 5 and customer.payment_method == 'AUTO'):
    offer_premium_support()

# After: Business rules as first-class concepts
class PremiumSupportEligibility:
    HIGH_VALUE_THRESHOLD = 10000
    MINIMUM_YEARS_ACTIVE = 2
    MAXIMUM_SUPPORT_TICKETS = 5

    def is_satisfied_by(self, customer):
        return (
            self._is_high_value_customer(customer) and
            self._is_long_term_customer(customer) and
            self._has_minimal_support_burden(customer) and
            self._has_automated_payment(customer)
        )

if PremiumSupportEligibility().is_satisfied_by(customer):
    offer_premium_support()
```

### Complex Construction as Narrative

Make object construction tell a story:

```python
invoice = (InvoiceBuilder()
    .for_customer(customer)
    .with_billing_period(Period.MONTHLY)
    .including_subscription_items(customer.active_subscriptions)
    .applying_promotional_discount(promo_code)
    .with_tax_jurisdiction(customer.tax_location)
    .due_within_days(30)
    .build())
```

Each method call reads like a requirement.

### Algorithms Named by Business Purpose

```python
class PremiumPricingStrategy:
    """20% markup for premium tier customers"""
    PREMIUM_MARKUP = 1.2

    def calculate(self, base_price):
        return base_price * self.PREMIUM_MARKUP

class DiscountPricingStrategy:
    """10% discount for bulk purchasers"""
    BULK_DISCOUNT = 0.9

    def calculate(self, base_price):
        return base_price * self.BULK_DISCOUNT
```

## Code Smells That Destroy Clarity

### The "And" Smell

If you need "and" in your function name, it's doing too much:

| Violates Single Responsibility | Fixed |
|--------------------------------|-------|
| `validate_and_save_user(user)` | `validate_user(user)`<br>`persist_user(user)` |
| `fetch_and_process_data(id)` | `fetch_data(id)`<br>`process_data(data)` |

### The "Utils" Catastrophe

"Utils" and "Helpers" are where self-documentation goes to die:

| Meaningless | Purposeful |
|-------------|------------|
| `class Utils:`<br>`  process(data)`<br>`  transform(obj)` | `class CustomerDataValidator:`<br>`  validate_email_format(email)`<br><br>`class PricingCalculator:`<br>`  apply_regional_adjustments(price, region)` |

### The Boolean Trap

Boolean parameters obscure intent:

| Obscure | Clear |
|---------|-------|
| `send_email(user, "Welcome!", True)` | `send_high_priority_email(user, "Welcome!")` |
| `process(data, False)` | `process_without_validation(data)` |

## Your Code as Domain Teacher

Your code should teach newcomers the business domain:

```python
class UnderwritingDecision:
    def evaluate_application(self, application):
        risk_score = self._calculate_actuarial_risk_score(application)

        if self._requires_reinsurance(risk_score):
            return self._refer_to_reinsurance_partner(application)

        premium = self._calculate_risk_adjusted_premium(risk_score)
        deductible = self._determine_appropriate_deductible(risk_score)

        return PolicyTerms(
            premium_monthly=premium,
            deductible=deductible,
            coverage_limits=self._standard_coverage_limits()
        )
```

A developer reading this learns:
- Underwriting involves risk scoring
- High risks might need reinsurance
- Premiums are risk-adjusted
- Policies have deductibles, limits, and coverage

The code has become documentation of the domain itself.

## The Hierarchy of Clarity

When making code self-documenting, follow this hierarchy:

| Rank | Approach |
|------|----------|
| **1. Best** | Make the code so clear it needs no explanation |
| **2. Good** | Restructure code to make intent obvious |
| **3. Acceptable** | Extract complex logic into well-named methods |
| **4. Last Resort** | Add a WHY comment (never a WHAT comment) |
| **5. Failure** | Leave unclear code with explanatory comments |

## The Refactoring Checklist

When reviewing code, ask:

1. Could I delete all comments and still understand everything?
2. Do names reflect business concepts, not technical implementation?
3. Does the code structure mirror how I'd explain this to a business person?
4. Are all magic values replaced with named constants that teach the domain?
5. Would a new developer learn the business by reading this code?

## The Curse of Knowledge

The biggest enemy of self-documenting code is your own expertise. You know too much. You've internalized the domain. What seems obvious to you is cryptic to others.

Write code for your past self from six months ago. That person who didn't know the domain, didn't understand the business rules, and couldn't guess what `proc_dt_calc` meant.

If that person could understand your code without any comments, without any documentation, without any hand-holding—you've achieved self-documenting code.

## Enforcement

Make this stick:

1. Reject PRs that rely on comments to explain WHAT the code does
2. Require business-domain names, not technical jargon
3. Ask reviewers: "Could you understand this without the comments?"
4. Treat unclear code as a bug, not a style issue

## The Choice

You have two paths:

**Path 1: Comments as Crutches**
- Write unclear code
- Add comments to explain it
- Watch comments drift from reality
- Accumulate lies in your codebase
- Force every new developer to decipher both code and comments
- Accept that understanding requires cross-referencing

**Path 2: Code That Speaks**
- Write code that teaches its own domain
- Use names that reveal intent
- Structure code like prose
- Make every constant a lesson
- Let new developers learn the business by reading the code
- Accept no substitutes for clarity

Choose Path 2. Delete your comments. Rewrite your code. Make it speak.

Every line of code you write is teaching someone about your domain. Make it a good teacher.
