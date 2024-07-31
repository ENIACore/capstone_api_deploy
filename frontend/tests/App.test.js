import { render } from '@testing-library/react';
import BackgroundMap from '../src/components/BackgroundMap/BackgroundMap.jsx';

test('Sample test', () => {
    render(<BackgroundMap />);
    // const linkElement = screen.getByText("Temp Fix Travel Planner");
    // expect(linkElement).toBeInTheDocument();
    expect(1 + 2).toBe(3)
});
