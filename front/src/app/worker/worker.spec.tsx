import { render } from '@testing-library/react';

import Worker from './worker';

describe('Worker', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<Worker />);
    expect(baseElement).toBeTruthy();
  });
});
